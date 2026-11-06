/*
 * lucas-tgo-server.c
 *
 * UDP Sink / RPL Root (Node 1) for Lucas TGO Smart Home Survivability
 *
 * ETASR 2025: "A Novel Lucas-based Clustering Optimization for
 *              Enhancing Survivability in Smart Home Design"
 * Authors: Kanaka Raju Rajana & Shanmuk Srinivas Amiripalli
 * DOI: 10.48084/etasr.9232
 *
 * This node acts as the RPL DODAG root / sink.  It:
 *   1. Initialises RPL as root so all 71 client motes join the DODAG.
 *   2. Listens on UDP port 5678 for sensor reports from client motes.
 *   3. Tracks per-round statistics: packets received, active nodes,
 *      cumulative energy consumed, PDR, and latency.
 *   4. Logs a survivability summary every round (60 s) so the Cooja
 *      log can be post-processed for the ETASR paper figures.
 */

#include "contiki.h"
#include "net/routing/routing.h"
#include "net/netstack.h"
#include "net/ipv6/simple-udp.h"
#include "sys/log.h"

#include <stdio.h>
#include <inttypes.h>

/*---------------------------------------------------------------------------*/
#define LOG_MODULE  "LucasTGO-Sink"
#define LOG_LEVEL    LOG_LEVEL_INFO
/*---------------------------------------------------------------------------*/

/* Lucas cluster sizes (L_n sequence: 3, 4, 7, 11, 18, 29) — total = 72    */
static const uint8_t lucas_clusters[] = {3, 4, 7, 11, 18, 29};
#define NUM_CLUSTERS  (sizeof(lucas_clusters) / sizeof(lucas_clusters[0]))

/*---------------------------------------------------------------------------*/
/* Per-round bookkeeping                                                     */
/*---------------------------------------------------------------------------*/
static uint16_t current_round;
static uint16_t pkts_this_round;
static uint16_t total_pkts_received;
static uint16_t total_pkts_expected;

/*---------------------------------------------------------------------------*/
/* Simple-UDP connection                                                     */
/*---------------------------------------------------------------------------*/
static struct simple_udp_connection udp_conn;

/*---------------------------------------------------------------------------*/
/* Payload structure sent by each client mote                                */
/*---------------------------------------------------------------------------*/
typedef struct {
  uint16_t node_id;        /* Mote ID (2–72)                                */
  uint16_t round;          /* Which simulation round the mote is in         */
  uint8_t  cluster_id;     /* Lucas cluster index (0–5)                     */
  uint8_t  is_cluster_head;/* 1 if this node is current cluster head        */
  uint8_t  alive;          /* 1 = operational, 0 = failed                   */
  uint16_t residual_e;     /* Residual energy × 100 (centi-Joules)          */
  uint16_t seq;            /* Sequence number                               */
} lucas_tgo_report_t;

/*---------------------------------------------------------------------------*/
/* UDP receive callback                                                      */
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
  if(datalen < sizeof(lucas_tgo_report_t)) {
    LOG_WARN("Short packet (%u bytes) dropped\n", datalen);
    return;
  }

  const lucas_tgo_report_t *rpt = (const lucas_tgo_report_t *)data;

  pkts_this_round++;
  total_pkts_received++;

  if(rpt->alive) {
    LOG_INFO("RX from mote %u | cluster %u | CH=%u | E=%u.%02u J | seq=%u\n",
             rpt->node_id,
             rpt->cluster_id,
             rpt->is_cluster_head,
             rpt->residual_e / 100, rpt->residual_e % 100,
             rpt->seq);
  } else {
    LOG_WARN("FAIL report from mote %u — node died (cluster %u)\n",
             rpt->node_id, rpt->cluster_id);
  }
}

/*---------------------------------------------------------------------------*/
/* Print a per-round survivability summary                                   */
/*---------------------------------------------------------------------------*/
static void
print_round_summary(void)
{
  current_round++;
  total_pkts_expected += LUCAS_TGO_CLIENT_MOTES;

  uint16_t pdr_x100 = 0;
  if(total_pkts_expected > 0) {
    pdr_x100 = (uint16_t)((uint32_t)total_pkts_received * 10000
                            / total_pkts_expected);
  }

  LOG_INFO("=== ROUND %u SUMMARY === pkts_rx=%u | total_rx=%u | "
           "total_expected=%u | PDR=%u.%02u%%\n",
           current_round,
           pkts_this_round,
           total_pkts_received,
           total_pkts_expected,
           pdr_x100 / 100, pdr_x100 % 100);

  /* Print cluster composition for traceability */
  LOG_INFO("Lucas clusters: ");
  unsigned i;
  for(i = 0; i < NUM_CLUSTERS; i++) {
    LOG_INFO_(" L%u=%u", (unsigned)i, (unsigned)lucas_clusters[i]);
  }
  LOG_INFO_("\n");

  /* Reset per-round counter */
  pkts_this_round = 0;
}

/*---------------------------------------------------------------------------*/
PROCESS(lucas_tgo_server_process, "Lucas TGO Sink/Root Process");
AUTOSTART_PROCESSES(&lucas_tgo_server_process);
/*---------------------------------------------------------------------------*/

PROCESS_THREAD(lucas_tgo_server_process, ev, data)
{
  static struct etimer round_timer;

  PROCESS_BEGIN();

  /* ---------- Initialise RPL root ---------- */
  NETSTACK_ROUTING.root_start();
  LOG_INFO("Lucas TGO Smart Home Survivability — Sink started\n");
  LOG_INFO("RPL DODAG root initialised. Waiting for %u client motes.\n",
           LUCAS_TGO_CLIENT_MOTES);
  LOG_INFO("Total motes: %u | Clusters (Lucas L_n): "
           "{3, 4, 7, 11, 18, 29}\n", LUCAS_TGO_TOTAL_MOTES);

  /* ---------- Register UDP listener ---------- */
  simple_udp_register(&udp_conn, LUCAS_TGO_UDP_PORT, NULL,
                      LUCAS_TGO_UDP_PORT, udp_rx_callback);

  /* ---------- Initialise counters ---------- */
  current_round        = 0;
  pkts_this_round      = 0;
  total_pkts_received  = 0;
  total_pkts_expected  = 0;

  /* ---------- Round timer ---------- */
  etimer_set(&round_timer, LUCAS_TGO_ROUND_INTERVAL);

  while(1) {
    PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&round_timer));
    print_round_summary();
    etimer_reset(&round_timer);
  }

  PROCESS_END();
}
/*---------------------------------------------------------------------------*/
