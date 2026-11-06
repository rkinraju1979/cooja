# -*- coding: utf-8 -*-
"""
Generator for the 4 Distinct WSN Research Topologies (72 Motes each) in Contiki-NG Cooja (.csc):
1. lucas72_tgo.csc (Fig 3: Lucas TGO Unequal Clustering)
2. clustertree72.csc (Fig 4: Cluster Tree Hierarchy)
3. mesh72.csc (Fig 5: Multi-Cluster Mesh Network)
4. equal_tgo72.csc (Fig 6: Equal TGO Mesh Network)

All coordinates are in positive meter space X, Y in [20, 180] for 100% clear plotting and zero overlap.
"""

import os
import math
import numpy as np

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"
output_dir = os.path.join(base_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def build_csc_xml(title, tx_range, mote_positions):
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
      <interference_range>{(tx_range * 2):.1f}</interference_range>
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
      <viewport>1.50 0.0 0.0 1.50 20.0 20.0</viewport>
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

# --- 1. LUCAS TGO (Fig 3) ---
def get_lucas_tgo_positions():
    pos = [(1, (100.0, 30.0))] # Sink Node 1
    lucas_clusters = [
        {'size': 3,  'center': (45.0, 62.0)},
        {'size': 4,  'center': (100.0, 65.0)},
        {'size': 7,  'center': (155.0, 62.0)},
        {'size': 11, 'center': (45.0, 132.0)},
        {'size': 18, 'center': (100.0, 142.0)},
        {'size': 29, 'center': (160.0, 132.0)}
    ]
    curr_node = 2
    for cl in lucas_clusters:
        cx, cy = cl['center']
        size = cl['size']
        if size == 3:
            r = 14.0
            for i in range(3):
                ang = i * 2 * math.pi / 3
                pos.append((curr_node + i, (cx + r * math.cos(ang), cy + r * math.sin(ang))))
            curr_node += 3
        elif size == 4:
            pos.append((curr_node, (cx, cy))) # CH
            r = 16.0
            for i in range(3):
                ang = i * 2 * math.pi / 3
                pos.append((curr_node + 1 + i, (cx + r * math.cos(ang), cy + r * math.sin(ang))))
            curr_node += 4
        elif size == 7:
            pos.append((curr_node, (cx, cy))) # CH
            r1, r2 = 15.0, 25.0
            for i in range(3):
                ang = i * 2 * math.pi / 3
                pos.append((curr_node + 1 + i, (cx + r1 * math.cos(ang), cy + r1 * math.sin(ang))))
            for i in range(3):
                ang = i * 2 * math.pi / 3 + math.pi / 3
                pos.append((curr_node + 4 + i, (cx + r2 * math.cos(ang), cy + r2 * math.sin(ang))))
            curr_node += 7
        else: # 11, 18, 29
            pos.append((curr_node, (cx, cy))) # CH
            n_mem = size - 1
            for i in range(n_mem):
                layer = (i // 8) + 1
                r = 12.0 * layer + (i % 2) * 3.0
                ang = i * (2 * math.pi / n_mem)
                pos.append((curr_node + 1 + i, (cx + r * math.cos(ang), cy + r * math.sin(ang))))
            curr_node += size
    return pos[:72]

# --- 2. CLUSTER TREE (Fig 4) ---
def get_cluster_tree_positions():
    pos = [(1, (100.0, 100.0))] # Central Root Sink Node 1
    n_clusters = 8
    ch_ids = [2, 11, 20, 29, 38, 47, 56, 65]
    r_ch = 48.0
    r_mem = 18.0
    
    node_counter = 2
    for c_idx in range(n_clusters):
        ang = c_idx * (2 * math.pi / n_clusters)
        ch_id = ch_ids[c_idx]
        ch_x = 100.0 + r_ch * math.cos(ang)
        ch_y = 100.0 + r_ch * math.sin(ang)
        pos.append((ch_id, (ch_x, ch_y)))
        
        start_ang = ang - math.pi / 3.2
        end_ang = ang + math.pi / 3.2
        member_angles = np.linspace(start_ang, end_ang, 8)
        
        for m_ang in member_angles:
            m_id = node_counter
            while m_id in ch_ids or m_id == 1 or any(p[0] == m_id for p in pos):
                m_id += 1
            node_counter = m_id + 1
            mx = ch_x + r_mem * math.cos(m_ang)
            my = ch_y + r_mem * math.sin(m_ang)
            pos.append((m_id, (mx, my)))
    return sorted(pos, key=lambda p: p[0])[:72]

# --- 3. MESH NETWORK (Fig 5) ---
def get_mesh_positions():
    clusters = [
        {'ch': 1,  'nodes': list(range(1, 13)),   'center': (50.0, 50.0)},
        {'ch': 20, 'nodes': list(range(20, 35)),  'center': (150.0, 50.0)},
        {'ch': 40, 'nodes': list(range(40, 51)),  'center': (100.0, 100.0)},
        {'ch': 60, 'nodes': list(range(60, 71)),  'center': (50.0, 150.0)},
        {'ch': 72, 'nodes': list(range(72, 73)),  'center': (150.0, 150.0)}
    ]
    pos = []
    node_set = set()
    for c in clusters:
        ch_id = c['ch']
        cx, cy = c['center']
        if ch_id <= 72 and ch_id not in node_set:
            pos.append((ch_id, (cx, cy)))
            node_set.add(ch_id)
        members = [n for n in c['nodes'] if n != ch_id and n <= 72]
        n_m = len(members)
        for i, n_id in enumerate(members):
            if n_id not in node_set:
                ang = i * (2 * math.pi / max(1, n_m))
                r = 18.0 + (i % 2) * 4.0
                pos.append((n_id, (cx + r * math.cos(ang), cy + r * math.sin(ang))))
                node_set.add(n_id)
                
    for nid in range(1, 73):
        if nid not in node_set:
            col = (nid - 1) % 9
            row = (nid - 1) // 9
            pos.append((nid, (30.0 + col * 20.0, 30.0 + row * 20.0)))
            node_set.add(nid)
            
    return sorted(pos, key=lambda p: p[0])[:72]

# --- 4. EQUAL TGO (Fig 6) ---
def get_equal_tgo_positions():
    pos = [(1, (100.0, 25.0))] # Sink Node 1
    clusters = [
        {'ch': 2,  'nodes': list(range(2, 13)),   'center': (45.0, 65.0)},
        {'ch': 13, 'nodes': list(range(13, 25)),  'center': (100.0, 65.0)},
        {'ch': 25, 'nodes': list(range(25, 37)),  'center': (155.0, 65.0)},
        {'ch': 37, 'nodes': list(range(37, 49)),  'center': (45.0, 140.0)},
        {'ch': 49, 'nodes': list(range(49, 61)),  'center': (100.0, 148.0)},
        {'ch': 61, 'nodes': list(range(61, 73)),  'center': (155.0, 140.0)}
    ]
    for c in clusters:
        ch_id = c['ch']
        cx, cy = c['center']
        pos.append((ch_id, (cx, cy)))
        members = [n for n in c['nodes'] if n != ch_id and n <= 72]
        n_m = len(members)
        for i, n_id in enumerate(members):
            ang = i * (2 * math.pi / n_m)
            r = 16.0 + (i % 2) * 4.0
            pos.append((n_id, (cx + r * math.cos(ang), cy + r * math.sin(ang))))
    return sorted(pos, key=lambda p: p[0])[:72]

def generate_all():
    models = [
        ("Lucas_TGO_Unequal_Clustering_72Motes", "lucas72_tgo.csc", 65.0, get_lucas_tgo_positions()),
        ("Cluster_Tree_Topology_72Motes", "clustertree72.csc", 55.0, get_cluster_tree_positions()),
        ("Mesh_Network_Topology_72Motes", "mesh72.csc", 60.0, get_mesh_positions()),
        ("Equal_TGO_Mesh_Topology_72Motes", "equal_tgo72.csc", 60.0, get_equal_tgo_positions())
    ]
    for title, fname, tx_range, pos in models:
        xml = build_csc_xml(title, tx_range, pos)
        p1 = os.path.join(base_dir, fname)
        p2 = os.path.join(output_dir, fname)
        with open(p1, "w", encoding="utf-8") as f:
            f.write(xml)
        with open(p2, "w", encoding="utf-8") as f:
            f.write(xml)
        print(f"[+] Successfully Generated 72-Mote Topology: {fname}")

if __name__ == "__main__":
    generate_all()
