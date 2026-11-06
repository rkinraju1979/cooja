/*
 * Contiki-NG Implementation of ETASR 2025 Paper:
 * "A Novel Lucas-based Clustering Optimization for Enhancing Survivability in Smart Home Design"
 * Target: Tmote Sky / TelosB (MSP430 / CC2420 - 48KB ROM Limit Optimized)
 */

#include "contiki.h"
#include "net/routing/routing.h"
#include "net/ipv6/simple-udp.h"
#include "net/netstack.h"
#include "sys/log.h"
#include "random.h"

#define LOG_MODULE "LucasTGO"
#define LOG_LEVEL LOG_LEVEL_NONE

#define UDP_PORT 5678
#define SURVIVABILITY_INTERVAL (10 * CLOCK_SECOND)

static const uint8_t lucas_clusters[] = {3, 4, 7, 11, 18, 29};
static uint8_t current_round = 0;
static uint8_t active_nodes = 72;
static bool is_cluster_head = false;
static struct simple_udp_connection udp_conn;

PROCESS(lucas_tgo_survivability_process, "Lucas TGO Smart Home Survivability Process");
AUTOSTART_PROCESSES(&lucas_tgo_survivability_process);

static void handle_random_node_failure(void)
{
  uint16_t rand_val = random_rand() % 100;
  if(rand_val < 10) { /* 10% failure probability per round */
    if(active_nodes > 0) active_nodes--;
  }
}

static void udp_rx_callback(struct simple_udp_connection *c,
                            const uip_ipaddr_t *sender_addr,
                            uint16_t sender_port,
                            const uip_ipaddr_t *receiver_addr,
                            uint16_t receiver_port,
                            const uint8_t *data,
                            uint16_t datalen)
{
}

PROCESS_THREAD(lucas_tgo_survivability_process, ev, data)
{
  static struct etimer periodic_timer;
  uint8_t payload[4];

  PROCESS_BEGIN();

  simple_udp_register(&udp_conn, UDP_PORT, NULL, UDP_PORT, udp_rx_callback);

  etimer_set(&periodic_timer, SURVIVABILITY_INTERVAL);

  while(1) {
    PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&periodic_timer));

    current_round++;
    handle_random_node_failure();

    payload[0] = current_round;
    payload[1] = active_nodes;
    payload[2] = is_cluster_head ? 1 : 0;
    payload[3] = lucas_clusters[current_round % 6];

    uip_ipaddr_t dest_ip;
    uip_create_linklocal_allnodes_mcast(&dest_ip);
    simple_udp_sendto(&udp_conn, payload, sizeof(payload), &dest_ip);

    etimer_reset(&periodic_timer);
  }

  PROCESS_END();
}
