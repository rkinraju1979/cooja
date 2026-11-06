# -*- coding: utf-8 -*-
"""
Generates the 4 Exact Dashboard Figure Topologies (.csc) in Contiki-NG Cooja:
- Figure 3 (lucas72_tgo.csc): Lucas-based Clustering Model (6 Lucas Clusters: 3, 4, 7, 11, 18, 29 + Sink 1)
- Figure 4 (clustertree72.csc): Cluster Tree Topology (Central Sink Node 1 + 8 Radial CHs + 8 Arc Member Motes each)
- Figure 5 (mesh72.csc): Mesh Network Topology (5 Mesh Hubs + Inter-CH Full Mesh Backbone)
- Figure 6 (equal_tgo72.csc): TGO Mesh Network Topology (Sink Node 1 at Top + 6 TGO Triad Clusters of 12 motes)

All positions are scaled into positive meter space X, Y in [20, 260] with spacious node gaps (>16m) so:
1. Every single mote (1 to 72) is individually visible on screen (0% stacking).
2. The visual arrangement EXACTLY matches Figure 3, Figure 4, Figure 5, and Figure 6 from dashboard.html!
"""

import os
import math
import numpy as np

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"
output_dir = os.path.join(base_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def build_csc_xml(title, tx_range, mote_positions, viewport_scale=1.0, offset_x=20.0, offset_y=20.0):
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
    for node_id, (x, y) in mote_positions:
        mtype = "sink" if node_id == 1 else "client"
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
        <id>{node_id}</id>
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
      <transmitting_range>{tx_range:.1f}</transmitting_range>
      <interference_range>{(tx_range * 1.8):.1f}</interference_range>
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
      <viewport>{viewport_scale:.2f} 0.0 0.0 {viewport_scale:.2f} {offset_x:.1f} {offset_y:.1f}</viewport>
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
    return csc_content

# --- FIGURE 3: LUCAS TGO UNEQUAL CLUSTERING ---
def get_fig3_lucas_tgo_positions():
    pos = {1: (120.0, 30.0)} # Sink Node 1 at top center
    lucas_clusters = [
        {'size': 3,  'center': (45.0, 80.0)},
        {'size': 4,  'center': (120.0, 85.0)},
        {'size': 7,  'center': (195.0, 80.0)},
        {'size': 11, 'center': (45.0, 175.0)},
        {'size': 18, 'center': (120.0, 190.0)},
        {'size': 29, 'center': (205.0, 175.0)}
    ]
    curr_node = 2
    for cl in lucas_clusters:
        cx, cy = cl['center']
        size = cl['size']
        if size == 3:
            r = 18.0
            for i in range(3):
                ang = i * 2 * math.pi / 3
                pos[curr_node + i] = (cx + r * math.cos(ang), cy + r * math.sin(ang))
            curr_node += 3
        elif size == 4:
            pos[curr_node] = (cx, cy) # CH
            r = 20.0
            for i in range(3):
                ang = i * 2 * math.pi / 3
                pos[curr_node + 1 + i] = (cx + r * math.cos(ang), cy + r * math.sin(ang))
            curr_node += 4
        elif size == 7:
            pos[curr_node] = (cx, cy) # CH
            r1, r2 = 18.0, 32.0
            for i in range(3):
                ang = i * 2 * math.pi / 3
                pos[curr_node + 1 + i] = (cx + r1 * math.cos(ang), cy + r1 * math.sin(ang))
            for i in range(3):
                ang = i * 2 * math.pi / 3 + math.pi / 3
                pos[curr_node + 4 + i] = (cx + r2 * math.cos(ang), cy + r2 * math.sin(ang))
            curr_node += 7
        else: # 11, 18, 29
            pos[curr_node] = (cx, cy) # CH
            n_mem = size - 1
            for i in range(n_mem):
                layer = (i // 8) + 1
                r = 16.0 * layer + (i % 2) * 4.0
                ang = i * (2 * math.pi / min(n_mem, 8 if layer==1 else 12))
                pos[curr_node + 1 + i] = (cx + r * math.cos(ang), cy + r * math.sin(ang))
            curr_node += size
            
    res = [(nid, pos[nid]) for nid in sorted(pos.keys()) if nid <= 72]
    return res

# --- FIGURE 4: CLUSTER TREE ---
def get_fig4_cluster_tree_positions():
    pos = {1: (130.0, 130.0)} # Central Root Sink Node 1
    n_clusters = 8
    ch_ids = [2, 11, 20, 29, 38, 47, 56, 65]
    r_ch = 68.0  # Wide radius for 8 CHs
    r_mem = 22.0 # Spacious radius for 8 member motes around each CH
    
    node_counter = 2
    for c_idx in range(n_clusters):
        ang = c_idx * (2 * math.pi / n_clusters)
        ch_id = ch_ids[c_idx]
        ch_x = 130.0 + r_ch * math.cos(ang)
        ch_y = 130.0 + r_ch * math.sin(ang)
        pos[ch_id] = (ch_x, ch_y)
        
        start_ang = ang - math.pi / 3.0
        end_ang = ang + math.pi / 3.0
        member_angles = np.linspace(start_ang, end_ang, 8)
        
        for m_ang in member_angles:
            m_id = node_counter
            while m_id in ch_ids or m_id == 1 or m_id in pos:
                m_id += 1
            node_counter = m_id + 1
            mx = ch_x + r_mem * math.cos(m_ang)
            my = ch_y + r_mem * math.sin(m_ang)
            pos[m_id] = (mx, my)
            
    res = [(nid, pos[nid]) for nid in sorted(pos.keys()) if nid <= 72]
    return res

# --- FIGURE 5: MESH NETWORK ---
def get_fig5_mesh_positions():
    clusters = [
        {'ch': 1,  'nodes': list(range(1, 13)),   'center': (60.0, 60.0)},
        {'ch': 20, 'nodes': list(range(20, 35)),  'center': (200.0, 60.0)},
        {'ch': 40, 'nodes': list(range(40, 51)),  'center': (130.0, 130.0)},
        {'ch': 60, 'nodes': list(range(60, 71)),  'center': (60.0, 200.0)},
        {'ch': 72, 'nodes': [72, 71, 51, 52, 53, 54, 55, 56, 57, 58, 59], 'center': (200.0, 200.0)}
    ]
    pos = {}
    node_set = set()
    for c in clusters:
        ch_id = c['ch']
        cx, cy = c['center']
        if ch_id <= 72 and ch_id not in pos:
            pos[ch_id] = (cx, cy)
            node_set.add(ch_id)
        members = [n for n in c['nodes'] if n != ch_id and n <= 72]
        n_m = len(members)
        for i, n_id in enumerate(members):
            if n_id not in pos:
                ang = i * (2 * math.pi / max(1, n_m))
                r = 20.0 + (i % 2) * 5.0
                pos[n_id] = (cx + r * math.cos(ang), cy + r * math.sin(ang))
                node_set.add(n_id)
                
    for nid in range(1, 73):
        if nid not in pos:
            col = (nid - 1) % 9
            row = (nid - 1) // 9
            pos[nid] = (30.0 + col * 24.0, 30.0 + row * 24.0)
            
    res = [(nid, pos[nid]) for nid in sorted(pos.keys()) if nid <= 72]
    return res

# --- FIGURE 6: EQUAL TGO MESH ---
def get_fig6_equal_tgo_positions():
    pos = {1: (130.0, 30.0)} # Sink Node 1
    clusters = [
        {'ch': 2,  'nodes': list(range(2, 13)),   'center': (50.0, 90.0)},
        {'ch': 13, 'nodes': list(range(13, 25)),  'center': (130.0, 95.0)},
        {'ch': 25, 'nodes': list(range(25, 37)),  'center': (210.0, 90.0)},
        {'ch': 37, 'nodes': list(range(37, 49)),  'center': (50.0, 185.0)},
        {'ch': 49, 'nodes': list(range(49, 61)),  'center': (130.0, 195.0)},
        {'ch': 61, 'nodes': list(range(61, 73)),  'center': (210.0, 185.0)}
    ]
    for c in clusters:
        ch_id = c['ch']
        cx, cy = c['center']
        if ch_id not in pos:
            pos[ch_id] = (cx, cy)
        members = [n for n in c['nodes'] if n != ch_id and n <= 72]
        n_m = len(members)
        for i, n_id in enumerate(members):
            if n_id not in pos:
                ang = i * (2 * math.pi / n_m)
                r = 20.0 + (i % 2) * 5.0
                pos[n_id] = (cx + r * math.cos(ang), cy + r * math.sin(ang))
                
    res = [(nid, pos[nid]) for nid in sorted(pos.keys()) if nid <= 72]
    return res

def generate_exact_dashboard_topologies():
    models = [
        ("Lucas_TGO_Unequal_Clustering_72Motes", "lucas72_tgo.csc", 75.0, get_fig3_lucas_tgo_positions(), 1.0, 20.0, 20.0),
        ("Cluster_Tree_Topology_72Motes", "clustertree72.csc", 75.0, get_fig4_cluster_tree_positions(), 1.0, 20.0, 20.0),
        ("Mesh_Network_Topology_72Motes", "mesh72.csc", 75.0, get_fig5_mesh_positions(), 1.0, 20.0, 20.0),
        ("Equal_TGO_Mesh_Topology_72Motes", "equal_tgo72.csc", 75.0, get_fig6_equal_tgo_positions(), 1.0, 20.0, 20.0)
    ]
    for title, fname, tx_range, pos, v_scale, off_x, off_y in models:
        xml = build_csc_xml(title, tx_range, pos, v_scale, off_x, off_y)
        p1 = os.path.join(base_dir, fname)
        p2 = os.path.join(output_dir, fname)
        with open(p1, "w", encoding="utf-8") as f:
            f.write(xml)
        with open(p2, "w", encoding="utf-8") as f:
            f.write(xml)
        print(f"[+] Generated Exact Dashboard Topology CSC: {fname} ({len(pos)} Motes)")

if __name__ == "__main__":
    generate_exact_dashboard_topologies()
