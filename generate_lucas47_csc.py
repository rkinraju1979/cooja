import os
import numpy as np

# Script to build Cooja lucas47.csc XML simulation file with 47 motes
csc_path = 'c:/Users/Kanaka Raju/Desktop/joy29/lucas47.csc'

# Define Lucas Series Ring parameters for 47 motes
lucas_series = [1, 3, 4, 7, 11, 18] # Ring 0: Sink Node 1 (0,0) + Gateway Node 2 (15,0)
ring_radii   = [30.0, 55.0, 85.0, 120.0, 160.0, 205.0]

motes_coords = [(0.0, 0.0), (15.0, 0.0)] # Node 1 (Sink) & Node 2

for ring_idx, n_nodes in enumerate(lucas_series):
    r = ring_radii[ring_idx]
    phase_offset = (ring_idx * 137.508) * (np.pi / 180.0)
    angles = np.linspace(0, 2 * np.pi, n_nodes, endpoint=False) + phase_offset
    for a in angles:
        motes_coords.append((round(r * np.cos(a), 2), round(r * np.sin(a), 2)))

motes_coords = motes_coords[:47]

# Build XML content for lucas47.csc
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
    <title>Lucas Series 47-Mote RPL-UDP Simulation</title>
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

# Generate <mote> entries for 47 motes
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
  <plugin>
    org.contikios.cooja.plugins.SimControl
    <width>280</width>
    <z>1</z>
    <height>160</height>
    <location_x>400</location_x>
    <location_y>0</location_y>
  </plugin>
  <plugin>
    org.contikios.cooja.plugins.Visualizer
    <plugin_config>
      <moterelations>true</moterelations>
      <skin>org.contikios.cooja.plugins.skins.IDVisualizerSkin</skin>
      <skin>org.contikios.cooja.plugins.skins.GridVisualizerSkin</skin>
      <skin>org.contikios.cooja.plugins.skins.TrafficVisualizerSkin</skin>
      <skin>org.contikios.cooja.plugins.skins.UDGMVisualizerSkin</skin>
      <viewport>0.9 0 0 0.9 200 200</viewport>
    </plugin_config>
    <width>400</width>
    <z>2</z>
    <height>400</height>
    <location_x>1</location_x>
    <location_y>1</location_y>
  </plugin>
  <plugin>
    org.contikios.cooja.plugins.LogListener
    <plugin_config>
      <filter />
      <formatted_time />
      <coloring />
    </plugin_config>
    <width>800</width>
    <z>3</z>
    <height>300</height>
    <location_x>400</location_x>
    <location_y>160</location_y>
  </plugin>
</simconf>""")

with open(csc_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(xml_parts))

print(f"[+] Created Cooja Simulation File: {csc_path} with 47 Motes!")
