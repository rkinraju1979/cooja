CONTIKI_PROJECT = lucas-adaptive-server lucas-adaptive-client
all: $(CONTIKI_PROJECT)

CONTIKI = ../..

# Enable RPL Routing & IPv6 Stack (UDP Only)
MAKE_ROUTING = MAKE_ROUTING_RPL_LITE
MAKE_NET = MAKE_NET_IPV6

# Enable Contiki-NG Small Footprint Mode for Sky Mote Bounds
SMALL = 1
WERROR = 0

# Force Project Config Include & Compiler ROM Size Optimizations
CFLAGS += -DPROJECT_CONF_H=\"project-conf.h\"
CFLAGS += -Os -ffunction-sections -fdata-sections
LDFLAGS += -Wl,--gc-sections

include $(CONTIKI)/Makefile.include

%.sky: %
	@echo "[+] Firmware compiled for target sky: $@"
