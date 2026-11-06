import os
import numpy as np

# Script to build Cooja lucas199.csc XML simulation file with 199 motes
csc_path = 'c:/Users/Kanaka Raju/Desktop/joy29/lucas199.csc'

# Define Lucas Series Clusters for 199 motes: 2 + 1 + 3 + 4 + 7 + 11 + 18 + 29 + 47 + 76 = 198 clients + 1 sink = 199 motes
lucas_clusters = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
cluster_radii  = [25.0, 45.0, 70.0, 100.0, 135.0, 175.0, 220.0, 270.0, 325.0, 390.0]

motes_coords = [(0.0, 0.0)] # Node 1 (Sink)

for c_idx, n_motes in enumerate(lucas_clusters):
    r = cluster_radii[c_idx]
    phase = c_idx * (137.508 * np.pi / 180.0)
    angles = np.linspace(0, 2 * np.pi, n_motes, endpoint=False) + phase
    for a in angles:
        motes_coords.append((round(r * np.cos(a), 2), round(r * np.sin(a), 2)))

motes_coords = motes_coords[:199]

# Build XML content for lucas199.csc
xml_parts = [
"""<?xml version='1.0' encoding='UTF-8'?>
<simconf>
  <project EXPORT="discard">[APPS_DIR]/mrm</project>
  <project EXPORT="discard">[APPS_DIR]/mspsim</project>
  <project EXPORT="discard">[APPS_DIR]/avrora</project>
  <project EXPORT="discard">[APPS_DIR]/serial_socket</project>
  <project EXPORT="discard">[APPS_DIR]/collect-view</project>
  <project EXPORT="discard">[APPS_DIR]/powertracker</project>
  <simulation>
    <title>Lucas Series 199-Mote RPL-UDP Simulation</title>
    <randomseed>123456</randomseed>
    <motedelay_us>1000000</motedelay_us>
    <radiomedium>
      org.contikios.cooja.radiomediums.UDGM
      <transmitting_range>120.0</transmitting_range>
      <interference_range>240.0</interference_range>
      <success_ratio_tx>1.0</success_ratio_tx>
      <success_ratio_rx>1.0</success_ratio_rx>
    </radiomedium>
    <events>
      <logoutput>40000</logoutput>
    </events>
    <!-- Sink motetype -->
    <motetype>
      org.contikios.cooja.mspmote.SkyMoteType
      <identifier>sink</identifier>
      <description>RPL-UDP sink (server)</description>
      <source EXPORT="discard">[CONTIKI_DIR]/examples/rpl-udp/udp-server.c</source>
      <commands EXPORT="discard">make TARGET=sky udp-server.sky</commands>
      <firmware EXPORT="copy">[CONTIKI_DIR]/examples/rpl-udp/build/sky/udp-server.sky</firmware>
      <moteinterface>org.contikios.cooja.interfaces.Position</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.RimeAddress</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.IPAddress</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.Mote2MoteRelations</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.MoteAttributes</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.MspClock</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.MspMoteID</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.SkyButton</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.SkyFlash</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.SkyCoffeeFilesystem</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.Msp802154Radio</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.MspSerial</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.SkyLED</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.MspDebugOutput</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.SkyTemperature</moteinterface>
    </motetype>
    <!-- Client motetype -->
    <motetype>
      org.contikios.cooja.mspmote.SkyMoteType
      <identifier>client</identifier>
      <description>RPL-UDP client node</description>
      <source EXPORT="discard">[CONTIKI_DIR]/examples/rpl-udp/udp-client.c</source>
      <commands EXPORT="discard">make TARGET=sky udp-client.sky</commands>
      <firmware EXPORT="copy">[CONTIKI_DIR]/examples/rpl-udp/build/sky/udp-client.sky</firmware>
      <moteinterface>org.contikios.cooja.interfaces.Position</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.RimeAddress</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.IPAddress</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.Mote2MoteRelations</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.MoteAttributes</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.MspClock</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.MspMoteID</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.SkyButton</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.SkyFlash</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.SkyCoffeeFilesystem</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.Msp802154Radio</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.MspSerial</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.SkyLED</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.MspDebugOutput</moteinterface>
      <moteinterface>org.contikios.cooja.mspmote.interfaces.SkyTemperature</moteinterface>
    </motetype>"""
]

for i, (x, y) in enumerate(motes_coords):
    mote_id = i + 1
    mtype = "sink" if mote_id == 1 else "client"
    xml_parts.append(f"""    <mote>
      <breakpoints />
      <interface_config>
        org.contikios.cooja.interfaces.Position
        <x>{x}</x>
        <y>{y}</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        org.contikios.cooja.mspmote.interfaces.MspClock
        <deviation>1.0</deviation>
      </interface_config>
      <interface_config>
        org.contikios.cooja.mspmote.interfaces.MspMoteID
        <id>{mote_id}</id>
      </interface_config>
      <motetype_identifier>{mtype}</motetype_identifier>
    </mote>""")

xml_parts.append("""  </simulation>
</simconf>""")

with open(csc_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(xml_parts))

print(f"[+] Created Cooja Simulation File: {csc_path} with 199 Motes!")
