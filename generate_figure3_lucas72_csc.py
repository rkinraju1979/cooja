# -*- coding: utf-8 -*-
"""
Generates Figure 3 Lucas-Based Unequal Clustering Model Cooja XML Simulation (.csc) for 72 Motes:
- Sink Node (Node 1) at Top-Center (0, -120)
- 6 Lucas Clusters matching Lucas Sequence L_n = {3, 4, 7, 11, 18, 28}
  * Cluster 1 (3 motes): CH Node 2, Members 3-4 (Radius R1 = 12m)
  * Cluster 2 (4 motes): CH Node 5, Members 6-8 (Radius R2 = 14m)
  * Cluster 3 (7 motes): CH Node 9, Members 10-15 (Radius R3 = 18m)
  * Cluster 4 (11 motes): CH Node 16, Members 17-26 (Radius R4 = 22m)
  * Cluster 5 (18 motes): CH Node 27, Members 28-44 (Radius R5 = 28m)
  * Cluster 6 (28 motes): CH Node 45, Members 46-72 (Radius R6 = 36m)
"""

import os
import math

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"
output_dir = os.path.join(base_dir, "output")

def get_figure3_lucas_positions():
    pos = []
    
    # 1. Sink Node (Node 1) at Top Center
    pos.append((0.0, -120.0))
    
    # 6 Lucas Cluster Specifications: (CH_X, CH_Y, count, radius)
    clusters = [
        (-30.0, -75.0, 3, 14.0),   # Cluster 1: 3 motes (CH Node 2 + 2 members)
        (30.0, -75.0, 4, 16.0),    # Cluster 2: 4 motes (CH Node 5 + 3 members)
        (-65.0, -15.0, 7, 20.0),   # Cluster 3: 7 motes (CH Node 9 + 6 members)
        (65.0, -15.0, 11, 24.0),   # Cluster 4: 11 motes (CH Node 16 + 10 members)
        (-60.0, 65.0, 18, 30.0),   # Cluster 5: 18 motes (CH Node 27 + 17 members)
        (60.0, 75.0, 28, 38.0)     # Cluster 6: 28 motes (CH Node 45 + 27 members)
    ]
    
    for cx, cy, count, radius in clusters:
        # Cluster Head Mote at center (cx, cy)
        pos.append((cx, cy))
        
        # Member motes distributed in a ring around CH
        num_members = count - 1
        for k in range(num_members):
            angle = (2 * math.pi / num_members) * k
            mx = cx + radius * math.cos(angle)
            my = cy + radius * math.sin(angle)
            pos.append((mx, my))
            
    return pos[:72]

def generate_figure3_csc():
    mote_positions = get_figure3_lucas_positions()
    
    motetypes_xml = """    <motetype>
      org.contikios.cooja.contikimote.ContikiMoteType
      <identifier>sink</identifier>
      <description>RPL-UDP Sink Server (Node 1)</description>
      <source EXPORT="discard">[CONFIG_DIR]/lucas-adaptive-server.c</source>
      <commands EXPORT="discard">make TARGET=cooja lucas-adaptive-server.cooja</commands>
      <moteinterface>org.contikios.cooja.interfaces.Position</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.Battery</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiVib</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiMoteID</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiRS232</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiBeeper</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.IPAddress</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiRadio</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiButton</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiPIR</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiClock</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiLED</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiCFS</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiEEPROM</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.Mote2MoteRelations</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.MoteAttributes</moteinterface>
      <symbols>false</symbols>
    </motetype>
    <motetype>
      org.contikios.cooja.contikimote.ContikiMoteType
      <identifier>client</identifier>
      <description>RPL-UDP Lucas Client Node (Nodes 2-72)</description>
      <source EXPORT="discard">[CONFIG_DIR]/lucas-adaptive-client.c</source>
      <commands EXPORT="discard">make TARGET=cooja lucas-adaptive-client.cooja</commands>
      <moteinterface>org.contikios.cooja.interfaces.Position</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.Battery</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiVib</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiMoteID</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiRS232</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiBeeper</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.IPAddress</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiRadio</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiButton</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiPIR</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiClock</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiLED</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiCFS</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiEEPROM</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.Mote2MoteRelations</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.MoteAttributes</moteinterface>
      <symbols>false</symbols>
    </motetype>"""

    motes_xml = ""
    for i, (x, y) in enumerate(mote_positions, start=1):
        mtype = "sink" if i == 1 else "client"
        motes_xml += f"""    <mote>
      <breakpoints />
      <interface_config>
        org.contikios.cooja.interfaces.Position
        <x>{x:.2f}</x>
        <y>{y:.2f}</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        org.contikios.cooja.contikimote.interfaces.ContikiMoteID
        <id>{i}</id>
      </interface_config>
      <motetype_identifier>{mtype}</motetype_identifier>
    </mote>\n"""

    csc_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<simconf>
  <simulation>
    <title>Lucas_TGO_Unequal_Clustering_72Motes</title>
    <randomseed>123456</randomseed>
    <motedelay_us>1000000</motedelay_us>
    <radiomedium>
      org.contikios.cooja.radiomediums.UDGM
      <transmitting_range>75.0</transmitting_range>
      <interference_range>140.0</interference_range>
      <success_ratio_tx>1.0</success_ratio_tx>
      <success_ratio_rx>1.0</success_ratio_rx>
    </radiomedium>
    <events>
      <logoutput>40000</logoutput>
    </events>
{motetypes_xml}
{motes_xml}  </simulation>
  <plugin>
    org.contikios.cooja.plugins.SimControl
    <width>280</width>
    <z>1</z>
    <height>160</height>
    <location_x>620</location_x>
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
      <skin>org.contikios.cooja.plugins.skins.MoteTypeVisualizerSkin</skin>
      <viewport>1.60 0.0 0.0 1.60 280.0 280.0</viewport>
    </plugin_config>
    <width>600</width>
    <z>2</z>
    <height>600</height>
    <location_x>0</location_x>
    <location_y>0</location_y>
  </plugin>
  <plugin>
    org.contikios.cooja.plugins.LogListener
    <plugin_config>
      <filter />
      <formatted_time />
      <coloring />
    </plugin_config>
    <width>1000</width>
    <z>3</z>
    <height>300</height>
    <location_x>620</location_x>
    <location_y>160</location_y>
  </plugin>
</simconf>"""
    
    p1 = os.path.join(base_dir, "lucas72_tgo.csc")
    p2 = os.path.join(output_dir, "lucas72_tgo.csc")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(csc_content)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(csc_content)
    print(f"[+] SUCCESS: Generated Figure 3 Lucas Unequal Clustering CSC: {p1}")

if __name__ == "__main__":
    generate_figure3_csc()
