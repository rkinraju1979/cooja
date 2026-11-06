/*
 * project-conf.h
 *
 * Lucas TGO Smart Home Survivability — Project Configuration
 * ETASR 2025: "A Novel Lucas-based Clustering Optimization for
 *              Enhancing Survivability in Smart Home Design"
 *
 * Authors: Kanaka Raju Rajana & Shanmuk Srinivas Amiripalli
 *          Department of CSE, GST, GITAM University, Visakhapatnam
 * DOI: 10.48084/etasr.9232
 */

#ifndef PROJECT_CONF_H_
#define PROJECT_CONF_H_

/*---------------------------------------------------------------------------*/
/* Logging                                                                   */
/*---------------------------------------------------------------------------*/
#define LOG_CONF_LEVEL_RPL       LOG_LEVEL_WARN
#define LOG_CONF_LEVEL_TCPIP     LOG_LEVEL_WARN
#define LOG_CONF_LEVEL_IPV6      LOG_LEVEL_WARN
#define LOG_CONF_LEVEL_6LOWPAN   LOG_LEVEL_WARN
#define LOG_CONF_LEVEL_MAC       LOG_LEVEL_WARN
#define LOG_CONF_LEVEL_FRAMER    LOG_LEVEL_WARN

/*---------------------------------------------------------------------------*/
/* Network stack                                                             */
/*---------------------------------------------------------------------------*/
/* RPL operates in storing mode for multi-hop smart-home topologies          */
#define RPL_CONF_MOP                   RPL_MOP_STORING_NO_MULTICAST

/*---------------------------------------------------------------------------*/
/* ContikiMAC RDC — tuned for 72-mote smart-home density                    */
/*---------------------------------------------------------------------------*/
/* Channel check rate: 8 Hz gives good balance for 72 motes                 */
#define NETSTACK_CONF_RDC_CHANNEL_CHECK_RATE  8

/*---------------------------------------------------------------------------*/
/* UDP application port                                                      */
/*---------------------------------------------------------------------------*/
#define LUCAS_TGO_UDP_PORT  5678

/*---------------------------------------------------------------------------*/
/* Lucas TGO parameters (from ETASR 2025 paper)                             */
/*---------------------------------------------------------------------------*/
/* Lucas sequence: L_n = {2, 1, 3, 4, 7, 11, 18, 29, 47, 76, ...}          */
/* Cluster sizes used in 72-mote network: {3, 4, 7, 11, 18, 29}            */
#define LUCAS_TGO_NUM_CLUSTERS             6
#define LUCAS_TGO_TOTAL_MOTES             72
#define LUCAS_TGO_CLIENT_MOTES            71   /* excluding sink */

/* Node failure probability per round (15% as per ETASR benchmark)          */
#define LUCAS_TGO_FAILURE_PROB_PERCENT     15

/* Simulation round interval (seconds) — each round = 60s real-time        */
#define LUCAS_TGO_ROUND_INTERVAL          (60 * CLOCK_SECOND)

/* Client send interval (seconds) — sensor data every 30s                   */
#define LUCAS_TGO_SEND_INTERVAL           (30 * CLOCK_SECOND)

/* Maximum number of survivability test rounds                              */
#define LUCAS_TGO_MAX_ROUNDS              15

#endif /* PROJECT_CONF_H_ */
