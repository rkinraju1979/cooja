# -*- coding: utf-8 -*-
"""
Generates 100% Guaranteed Non-Overlapping 72-Mote Cooja Simulation Files (.csc)
Uses 25m uniform spacing across 9 columns x 8 rows in positive meter space X=[30..230], Y=[30..205].
Guarantees every single one of the 72 motes (Node 1 through Node 72) is clearly visible and perfectly arranged on Cooja's Network Window.
"""

import os

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"
output_dir = os.path.join(base_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_spacious_csc(title, filename):
    # 9 columns x 8 rows = 72 motes
    mote_positions = []
    col_spacing = 25.0
    row_spacing = 25.0
    
    for row in range(8):
        for col in range(9):
            x = 30.0 + col * col_spacing
            y = 30.0 + row * row_spacing
            mote_positions.append((x, y))

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
    <title>{title}</title>
    <randomseed>123456</randomseed>
    <motedelay_us>1000000</motedelay_us>
    <radiomedium>
      org.contikios.cooja.radiomediums.UDGM
      <transmitting_range>75.0</transmitting_range>
      <interference_range>150.0</interference_range>
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
    <width>280</width><z>1</z><height>160</height><location_x>620</location_x><location_y>0</location_y>
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
      <viewport>1.20 0.0 0.0 1.20 20.0 20.0</viewport>
    </plugin_config>
    <width>600</width><z>2</z><height>600</height><location_x>0</location_x><location_y>0</location_y>
  </plugin>
  <plugin>
    org.contikios.cooja.plugins.LogListener
    <plugin_config>
      <filter /><formatted_time /><coloring />
    </plugin_config>
    <width>1000</width><z>3</z><height>300</height><location_x>620</location_x><location_y>160</location_y>
  </plugin>
</simconf>"""

    p1 = os.path.join(base_dir, filename)
    p2 = os.path.join(output_dir, filename)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(csc_content)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(csc_content)
    print(f"[+] Successfully Generated Spacious CSC: {filename}")

if __name__ == "__main__":
    generate_spacious_csc("Lucas_TGO_Grid_72Motes", "lucas72_tgo.csc")
    generate_spacious_csc("Cluster_Tree_Grid_72Motes", "clustertree72.csc")
    generate_spacious_csc("Mesh_Grid_72Motes", "mesh72.csc")
    generate_spacious_csc("Equal_TGO_Grid_72Motes", "equal_tgo72.csc")
