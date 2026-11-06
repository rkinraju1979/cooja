##############################################################################
# Makefile — Lucas TGO Smart Home Survivability
#
# ETASR 2025: "A Novel Lucas-based Clustering Optimization for
#              Enhancing Survivability in Smart Home Design"
#
# Build targets:
#   lucas-tgo-server   (Sink node — Node 1)
#   lucas-tgo-client   (Client nodes — Nodes 2–72)
#
# Usage:
#   make TARGET=cooja             # Build both for Cooja simulator
#   make TARGET=cooja clean       # Clean build artifacts
#
# IMPORTANT: Set CONTIKI to your Contiki-NG installation path.
#            Example: CONTIKI = /home/user/contiki-ng
##############################################################################

CONTIKI_PROJECT  = lucas-tgo-server lucas-tgo-client
all: $(CONTIKI_PROJECT)

# ---- Set your Contiki-NG path here ----
# If CONTIKI is not already set in your environment, uncomment and edit:
# CONTIKI = /path/to/contiki-ng

# Project configuration
PROJECTDIRS += .
PROJECT_CONF_H = project-conf.h

# Include the Contiki-NG build system
include $(CONTIKI)/Makefile.include
