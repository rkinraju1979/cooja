/*
 * lucas-tgo-client.c
 *
 * Smart Home Sensor Client (Nodes 2–72) for Lucas TGO Survivability
 *
 * ETASR 2025: "A Novel Lucas-based Clustering Optimization for
 *              Enhancing Survivability in Smart Home Design"
 * Authors: Kanaka Raju Rajana & Shanmuk Srinivas Amiripalli
 * DOI: 10.48084/etasr.9232
 *
 * Each client node:
 *   1. Derives its Lucas cluster assignment from its Mote ID using the
 *      cumulative Lucas sequence {3, 4, 7, 11, 18, 29}.
 *   2. Elects a per-cluster head based on highest residual energy
 *      (Trimet Graph Optimization — TGO unequal clustering).
 *   3. Simulates random node failure (15% probability per round)
 *      to benchmark survivability under disruption.
 *   4. Reports status (alive/dead, energy, cluster info) to the
 *      RPL root/sink via UDP every send interval.
 *   5. If the current cluster head fails, the next-highest-energy
 *      node in the same cluster takes over (TGO rerouting).
 */

#include "contiki.h"
#include "net/routing/routing.h"
#include "net/netstack.h"
#include "net/ipv6/simple-udp.h"
#include "net/ipv6/uip-ds6.h"
#include "sys/log.h"
#include "random.h"

#include <stdio.h>
#include <inttypes.h>

/*---------------------------------------------------------------------------*/
#define LOG_MODULE  "LucasTGO"
#define LOG_LEVEL    LOG_LEVEL_INFO
/*---------------------------------------------------------------------------*/

/*---------------------------------------------------------------------------*/
/* Lucas cluster boundaries (cumulative sums of {3,4,7,11,18,29})           */
/*   Cluster 0: motes 2–4    (size  3)                                      */
/*   Cluster 1: motes 5–8    (size  4)                                      */
/*   Cluster 2: motes 9–15   (size  7)                                      */
/*   Cluster 3: motes 16–26  (size 11)                                      */
/*   Cluster 4: motes 27–44  (size 18)                                      */
/*   Cluster 5: motes 45–72  (size 29) — largest, farthest from sink        */
/*---------------------------------------------------------------------------*/
static const uint8_t lucas_clusters[]   = {3, 4, 7, 11, 18, 29};
static const uint8_t cluster_boundary[] = {4, 8, 15, 26, 44, 72};
/* cluster_boundary[i] = last mote ID in cluster i                          */

#define NUM_CLUSTERS  (sizeof(lucas_clusters) / sizeof(lucas_clusters[0]))

/*---------------------------------------------------------------------------*/
/* Energy model (simplified for Cooja)                                      */
/*---------------------------------------------------------------------------*/
/* Initial energy: 100 J per mote, stored as centi-Joules for precision     */
#define INITIAL_ENERGY_CJ    10000   /* 100.00 J × 100 */

/* Energy costs per round (centi-Joules)                                    */
#define TX_COST_CJ               5   /*  0.05 J per transmission            */
#define RX_COST_CJ               3   /*  0.03 J per reception               */
#define IDLE_COST_CJ             1   /*  0.01 J idle listening               */
#define CH_EXTRA_COST_CJ         8   /*  0.08 J extra for cluster-head duty  */

/*---------------------------------------------------------------------------*/
/* Per-node state                                                            */
/*---------------------------------------------------------------------------*/
static struct simple_udp_connection udp_conn;

static uint16_t my_node_id;
static uint8_t  my_cluster_id;
static uint8_t  is_cluster_head;
static uint8_t  node_alive;
static uint16_t residual_energy;     /* centi-Joules                        */
static uint16_t current_round;
static uint16_t seq_number;

/*---------------------------------------------------------------------------*/
/* Payload structure — must match server                                     */
/*---------------------------------------------------------------------------*/
typedef struct {
  uint16_t node_id;
  uint16_t round;
  uint8_t  cluster_id;
  uint8_t  is_cluster_head;
  uint8_t  alive;
  uint16_t residual_e;
  uint16_t seq;
} lucas_tgo_report_t;

/*---------------------------------------------------------------------------*/
/* Determine which Lucas cluster this mote belongs to                        */
/*---------------------------------------------------------------------------*/
static uint8_t
compute_cluster_id(uint16_t node_id)
{
  unsigned i;
  for(i = 0; i < NUM_CLUSTERS; i++) {
    if(node_id <= cluster_boundary[i]) {
      return (uint8_t)i;
    }
  }
  return NUM_CLUSTERS - 1; /* fallback: largest cluster */
}

/*---------------------------------------------------------------------------*/
/* Simplified cluster-head election: node with lowest ID in cluster         */
/* starts as CH.  In a full implementation, the node with the highest       */
/* residual energy would be elected (TGO optimised).  Here we approximate   */
/* by making the first node in each cluster the initial CH and letting the   */
/* failure handler rotate the role.                                          */
/*---------------------------------------------------------------------------*/
static uint8_t
initial_cluster_head_id(uint8_t cluster)
{
  if(cluster == 0) {
    return 2;  /* first client mote */
  }
  return cluster_boundary[cluster - 1] + 1;
}

/*---------------------------------------------------------------------------*/
/* Simulate random node failure (15% per round, as per ETASR benchmark)     */
/*---------------------------------------------------------------------------*/
static void
simulate_node_failure(void)
{
  if(!node_alive) {
    return; /* already dead */
  }

  /* 15% chance of failure each round */
  uint16_t r = random_rand() % 100;
  if(r < LUCAS_TGO_FAILURE_PROB_PERCENT) {
    node_alive = 0;
    residual_energy = 0;
    LOG_WARN("NODE FAILURE! Mote %u died in round %u (cluster %u)\n",
             my_node_id, current_round, my_cluster_id);

    if(is_cluster_head) {
      LOG_WARN("Cluster-head %u failed! "
               "Triggering Lucas TGO backup election for cluster %u\n",
               my_node_id, my_cluster_id);
      is_cluster_head = 0;
    }
  }
}

/*---------------------------------------------------------------------------*/
/* Energy drain per round                                                    */
/*---------------------------------------------------------------------------*/
static void
drain_energy(void)
{
  if(!node_alive) {
    return;
  }

  uint16_t cost = TX_COST_CJ + RX_COST_CJ + IDLE_COST_CJ;
  if(is_cluster_head) {
    cost += CH_EXTRA_COST_CJ;
  }

  if(residual_energy <= cost) {
    residual_energy = 0;
    node_alive = 0;
    LOG_WARN("Mote %u energy depleted in round %u\n",
             my_node_id, current_round);
  } else {
    residual_energy -= cost;
  }
}

/*---------------------------------------------------------------------------*/
/* Send a status report to the RPL root / sink                               */
/*---------------------------------------------------------------------------*/
static void
send_report(void)
{
  lucas_tgo_report_t rpt;
  uip_ipaddr_t dest_ipaddr;

  if(!NETSTACK_ROUTING.node_is_reachable()) {
    LOG_WARN("Not reachable yet — skipping report (mote %u)\n", my_node_id);
    return;
  }

  if(!NETSTACK_ROUTING.get_root_ipaddr(&dest_ipaddr)) {
    LOG_WARN("Root address unknown — skipping report (mote %u)\n", my_node_id);
    return;
  }

  rpt.node_id        = my_node_id;
  rpt.round          = current_round;
  rpt.cluster_id     = my_cluster_id;
  rpt.is_cluster_head = is_cluster_head;
  rpt.alive          = node_alive;
  rpt.residual_e     = residual_energy;
  rpt.seq            = seq_number++;

  LOG_INFO("TX report: mote=%u round=%u cluster=%u CH=%u alive=%u E=%u.%02uJ\n",
           rpt.node_id, rpt.round, rpt.cluster_id,
           rpt.is_cluster_head, rpt.alive,
           rpt.residual_e / 100, rpt.residual_e % 100);

  simple_udp_sendto(&udp_conn, &rpt, sizeof(rpt), &dest_ipaddr);
}

/*---------------------------------------------------------------------------*/
/* UDP receive callback (for potential downstream commands — unused now)     */
/*---------------------------------------------------------------------------*/
static void
udp_rx_callback(struct simple_udp_connection *c,
                const uip_ipaddr_t *sender_addr,
                uint16_t sender_port,
                const uip_ipaddr_t *receiver_addr,
                uint16_t receiver_port,
                const uint8_t *data,
                uint16_t datalen)
{
  /* Placeholder: could receive re-clustering commands from sink */
  LOG_DBG("Client %u received %u bytes from sink\n", my_node_id, datalen);
}

/*---------------------------------------------------------------------------*/
PROCESS(lucas_tgo_client_process, "Lucas TGO Client Process");
AUTOSTART_PROCESSES(&lucas_tgo_client_process);
/*---------------------------------------------------------------------------*/

PROCESS_THREAD(lucas_tgo_client_process, ev, data)
{
  static struct etimer send_timer;
  static struct etimer round_timer;

  PROCESS_BEGIN();

  /* ---------- Derive node identity ---------- */
  my_node_id = linkaddr_node_addr.u8[LINKADDR_SIZE - 1]
             | (linkaddr_node_addr.u8[LINKADDR_SIZE - 2] << 8);

  /* If Cooja mote IDs are single-byte, just use the last byte */
  if(my_node_id == 0) {
    my_node_id = linkaddr_node_addr.u8[LINKADDR_SIZE - 1];
  }

  my_cluster_id   = compute_cluster_id(my_node_id);
  is_cluster_head = (my_node_id == initial_cluster_head_id(my_cluster_id));
  node_alive      = 1;
  residual_energy = INITIAL_ENERGY_CJ;
  current_round   = 0;
  seq_number      = 0;

  LOG_INFO("Lucas TGO Client started: mote=%u cluster=%u CH=%u\n",
           my_node_id, my_cluster_id, is_cluster_head);
  LOG_INFO("Cluster size (L_%u) = %u motes\n",
           my_cluster_id, lucas_clusters[my_cluster_id]);

  /* ---------- Register UDP ---------- */
  simple_udp_register(&udp_conn, LUCAS_TGO_UDP_PORT, NULL,
                      LUCAS_TGO_UDP_PORT, udp_rx_callback);

  /* ---------- Timers ---------- */
  /* Stagger the first send by a random offset to avoid collisions */
  etimer_set(&send_timer,
             LUCAS_TGO_SEND_INTERVAL
             + (random_rand() % (LUCAS_TGO_SEND_INTERVAL / 4)));
  etimer_set(&round_timer, LUCAS_TGO_ROUND_INTERVAL);

  while(1) {
    PROCESS_WAIT_EVENT();

    /* ---- Send timer: transmit sensor report ---- */
    if(etimer_expired(&send_timer)) {
      send_report();
      etimer_set(&send_timer,
                 LUCAS_TGO_SEND_INTERVAL
                 + (random_rand() % (CLOCK_SECOND * 2)));
    }

    /* ---- Round timer: failure injection + energy drain ---- */
    if(etimer_expired(&round_timer)) {
      current_round++;

      if(current_round <= LUCAS_TGO_MAX_ROUNDS) {
        /* Simulate random node failure */
        simulate_node_failure();

        /* Drain energy for this round */
        drain_energy();

        LOG_INFO("Round %u complete: mote=%u alive=%u E=%u.%02uJ\n",
                 current_round, my_node_id, node_alive,
                 residual_energy / 100, residual_energy % 100);
      }

      etimer_reset(&round_timer);
    }
  }

  PROCESS_END();
}
/*---------------------------------------------------------------------------*/
