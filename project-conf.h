/*
 * Contiki-NG Project Configuration Header
 * Target: Cooja / Native Mote (Logging Enabled)
 * IJ-ICT 2026 Reference Implementation: Lucas Adaptive Sampling Strategy (LASS)
 */

#ifndef PROJECT_CONF_H_
#define PROJECT_CONF_H_

/* Undefine command-line overrides to prevent GCC redefinition errors */
#undef LOG_CONF_LEVEL_RPL
#undef LOG_CONF_LEVEL_TCPIP
#undef LOG_CONF_LEVEL_IPV6
#undef LOG_CONF_LEVEL_MAC
#undef LOG_CONF_LEVEL_MAIN
#undef UIP_CONF_TCP

/* Set project bounds */
#define UIP_CONF_TCP 0
#define ENEREST_CONF_ON 1
#define ROUTING_CONF_RPL_LITE 1

#define LOG_CONF_LEVEL_RPL LOG_LEVEL_INFO
#define LOG_CONF_LEVEL_TCPIP LOG_LEVEL_INFO
#define LOG_CONF_LEVEL_IPV6 LOG_LEVEL_INFO
#define LOG_CONF_LEVEL_MAC LOG_LEVEL_INFO
#define LOG_CONF_LEVEL_MAIN LOG_LEVEL_INFO

#endif /* PROJECT_CONF_H_ */
