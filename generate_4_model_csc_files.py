# -*- coding: utf-8 -*-
"""
Generator for Contiki-NG Cooja XML Simulation Configurations (.csc) for all 4 Smart Home Topologies (72 Motes each):
Uses standard Cooja [CONFIG_DIR] path variable so Cooja executes make inside whichever folder the .csc file is loaded from.
"""

import os
import math

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"
output_dir = os.path.join(base_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_csc_xml(title, mote_positions):
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
      <transmitting_range>60.0</transmitting_range>
      <interference_range>120.0</interference_range>
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
      <viewport>1.80 0.0 0.0 1.80 300.0 300.0</viewport>
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
    return csc_content

def get_grid_positions():
    mote_positions = []
    col_spacing = 20.0
    row_spacing = 20.0
    for row in range(8):
        for col in range(9):
            x = (col - 4) * col_spacing
            y = (row - 4) * row_spacing
            mote_positions.append((x, y))
    return mote_positions[:72]

def generate_all_csc():
    models = [
        ("Lucas_TGO_Unequal_Clustering_72Motes", "lucas72_tgo.csc", get_grid_positions()),
        ("Cluster_Tree_Topology_72Motes", "clustertree72.csc", get_grid_positions()),
        ("Mesh_Network_Topology_72Motes", "mesh72.csc", get_grid_positions()),
        ("Equal_TGO_Mesh_Topology_72Motes", "equal_tgo72.csc", get_equaltgo_positions() if 'get_equaltgo_positions' in globals() else get_grid_positions())
    ]
    
    for title, fname, pos in models:
        xml_content = generate_csc_xml(title, pos)
        p1 = os.path.join(base_dir, fname)
        p2 = os.path.join(output_dir, fname)
        with open(p1, "w", encoding="utf-8") as f:
            f.write(xml_content)
        with open(p2, "w", encoding="utf-8") as f:
            f.write(xml_content)
        print(f"[+] Saved Standard CONFIG_DIR CSC: {p1} AND {p2}")

if __name__ == "__main__":
    generate_all_csc()
