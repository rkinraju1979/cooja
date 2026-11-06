/*
 * Contiki-NG RPL-UDP Universal Hierarchical Clustering Client
 * Target: Cooja / Native Mote (Logging Enabled)
 * Reference Implementation: Kanaka Raju Rajana & Shanmuk Srinivas Amiripalli
 */

#include "contiki.h"
#include "net/routing/routing.h"
#include "net/netstack.h"
#include "net/ipv6/simple-udp.h"
#include "sys/log.h"
#include "random.h"
#include "net/linkaddr.h"
#include <string.h>
#include <stdio.h>

#define LOG_MODULE "Lucas-Client"
#define LOG_LEVEL LOG_LEVEL_INFO

#define UDP_CLIENT_PORT 8765
#define UDP_SERVER_PORT 5678

static struct simple_udp_connection udp_conn_sink;

/* Lucas Sequence for Adaptive Sampling Intervals (seconds) */
static const uint8_t lucas_seq[] = {2, 1, 3, 4, 7, 11, 18, 29};
static uint8_t lucas_idx = 0;

PROCESS(lucas_client_process, "Universal RPL-UDP Hierarchical Clustering Client");
AUTOSTART_PROCESSES(&lucas_client_process);

static clock_time_t get_next_sampling_interval(void) {
  clock_time_t interval_sec = lucas_seq[lucas_idx];
  lucas_idx = (lucas_idx + 1) % 8;
  return interval_sec * CLOCK_SECOND;
}

PROCESS_THREAD(lucas_client_process, ev, data)
{
  static struct etimer periodic_timer;
  static char payload[64];
  static uint32_t seq_id = 0;
  uip_ipaddr_t dest_ipaddr;

  PROCESS_BEGIN();

  /* Register Simple UDP Connection with Server (Sink) */
  simple_udp_register(&udp_conn_sink, UDP_CLIENT_PORT, NULL,
                      UDP_SERVER_PORT, NULL);

  LOG_INFO("Client Process Started. Waiting for RPL DODAG Join...\n");

  /* Wait 5 seconds for RPL Network DODAG to Form */
  etimer_set(&periodic_timer, CLOCK_SECOND * 5);
  PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&periodic_timer));

  while(1) {
    clock_time_t interval = get_next_sampling_interval();
    etimer_set(&periodic_timer, interval);
    PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&periodic_timer));

    if(NETSTACK_ROUTING.node_is_reachable() && NETSTACK_ROUTING.get_root_ipaddr(&dest_ipaddr)) {
      seq_id++;
      snprintf(payload, sizeof(payload), "LUCAS-DATA #%lu ID=%u", (unsigned long)seq_id, linkaddr_node_addr.u8[7]);
      simple_udp_sendto(&udp_conn_sink, payload, strlen(payload), &dest_ipaddr);
      LOG_INFO("Sent Packet #%lu to Sink (Interval = %u s)\n", (unsigned long)seq_id, (unsigned int)(interval / CLOCK_SECOND));
    } else {
      LOG_INFO("Waiting for RPL reachable root...\n");
    }
  }

  PROCESS_END();
}
