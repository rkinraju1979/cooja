/*
 * Contiki-NG RPL-UDP Lucas-Based Adaptive Sampling Server (RPL Root Sink)
 * Target: Cooja / Native Mote (Logging Enabled)
 * Reference Implementation: Kanaka Raju Rajana & Shanmuk Srinivas Amiripalli
 */

#include "contiki.h"
#include "net/routing/routing.h"
#include "net/netstack.h"
#include "net/ipv6/simple-udp.h"
#include "sys/log.h"

#define LOG_MODULE "Lucas-Server"
#define LOG_LEVEL LOG_LEVEL_INFO

#define UDP_CLIENT_PORT 8765
#define UDP_SERVER_PORT 5678

static struct simple_udp_connection udp_conn;

PROCESS(lucas_server_process, "Lucas-Based Adaptive Sampling Server Process");
AUTOSTART_PROCESSES(&lucas_server_process);

static void udp_rx_callback(struct simple_udp_connection *c,
                            const uip_ipaddr_t *sender_addr,
                            uint16_t sender_port,
                            const uip_ipaddr_t *receiver_addr,
                            uint16_t receiver_port,
                            const uint8_t *data,
                            uint16_t datalen)
{
  uint8_t sender_id = sender_addr->u8[15];
  LOG_INFO("DATA RX from Node %u: %s (datalen=%u)\n", sender_id, (const char *)data, datalen);
}

PROCESS_THREAD(lucas_server_process, ev, data)
{
  PROCESS_BEGIN();

  LOG_INFO("Initializing RPL DODAG Root Server (Node 1)...\n");

  /* Initialize RPL DODAG Root */
  NETSTACK_ROUTING.root_start();

  /* Register Simple UDP listener matching client port configuration */
  simple_udp_register(&udp_conn, UDP_SERVER_PORT, NULL,
                      UDP_CLIENT_PORT, udp_rx_callback);

  LOG_INFO("Server Listening on UDP Port %u (Client Port %u)\n", UDP_SERVER_PORT, UDP_CLIENT_PORT);

  PROCESS_END();
}
