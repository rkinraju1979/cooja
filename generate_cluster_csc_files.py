import os
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = script_dir if script_dir else os.getcwd()

print("[+] Generating Optimized Cooja .csc Simulation Files with Extended UDGM Coverage...")

folder_name = os.path.basename(base_dir)

def generate_csc_file(filename, sim_name, coords):
    csc_path = os.path.join(base_dir, filename)
    
    xml_parts = [
        f"""<?xml version="1.0" encoding="UTF-8"?>
<simconf>
  <project EXPORT="discard">[APPS_DIR]/mspsim</project>
  <project EXPORT="discard">[APPS_DIR]/serial_socket</project>
  <project EXPORT="discard">[APPS_DIR]/powertracker</project>
  <simulation>
    <title>{sim_name}</title>
    <randomseed>123456</randomseed>
    <motedelay_us>1000000</motedelay_us>
    <radiomedium>
      org.contikios.cooja.radiomediums.UDGM
      <transmitting_range>180.0</transmitting_range>
      <interference_range>360.0</interference_range>
      <success_ratio_tx>1.0</success_ratio_tx>
      <success_ratio_rx>1.0</success_ratio_rx>
    </radiomedium>
    <events>
      <logoutput>40000</logoutput>
    </events>
    <motetype>
      org.contikios.cooja.mspmote.SkyMoteType
      <identifier>sink</identifier>
      <description>RPL-UDP Server Sink</description>
      <source EXPORT="discard">[CONTIKI_DIR]/examples/{folder_name}/lucas-adaptive-server.c</source>
      <commands EXPORT="discard">make TARGET=sky lucas-adaptive-server</commands>
      <firmware EXPORT="copy">[CONTIKI_DIR]/examples/{folder_name}/build/sky/lucas-adaptive-server.sky</firmware>
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
    <motetype>
      org.contikios.cooja.mspmote.SkyMoteType
      <identifier>client</identifier>
      <description>Lucas Adaptive Client</description>
      <source EXPORT="discard">[CONTIKI_DIR]/examples/{folder_name}/lucas-adaptive-client.c</source>
      <commands EXPORT="discard">make TARGET=sky lucas-adaptive-client</commands>
      <firmware EXPORT="copy">[CONTIKI_DIR]/examples/{folder_name}/build/sky/lucas-adaptive-client.sky</firmware>
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

    for i, (x, y) in enumerate(coords):
        mote_id = i + 1
        mtype = "sink" if mote_id == 1 else "client"
        xml_parts.append(f"""    <mote>
      <breakpoints />
      <interface_config>
        org.contikios.cooja.interfaces.Position
        <x>{x:.2f}</x>
        <y>{y:.2f}</y>
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
    <skin>org.contikios.cooja.plugins.skins.IDVisualizerSkin</skin>
    <skin>org.contikios.cooja.plugins.skins.GridVisualizerSkin</skin>
    <skin>org.contikios.cooja.plugins.skins.TrafficVisualizerSkin</skin>
    <skin>org.contikios.cooja.plugins.skins.UDGMVisualizerSkin</skin>
    <width>500</width>
    <z>2</z>
    <height>500</height>
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
    <width>1100</width>
    <z>3</z>
    <height>300</height>
    <location_x>400</location_x>
    <location_y>160</location_y>
  </plugin>
</simconf>""")

    with open(csc_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_parts))
    print(f"[+] Generated Cooja Simulation File: {csc_path}")

# 1. Low Density Coordinates (20 clusters x 5 nodes = 100 clients + 1 Sink Node 1 = 101 motes)
coords_low = [(0.0, -160.0)]  # Dedicated RPL Root Sink Node 1 (Top Center, Visible)
for r in range(4):
    for c in range(5):
        if len(coords_low) >= 101: break
        cx, cy = c * 70.0 - 140.0, r * 70.0 - 90.0
        coords_low.append((cx, cy))  # Cluster Head
        for i in range(4):
            if len(coords_low) >= 101: break
            ang = i * (2 * np.pi / 4.0)
            coords_low.append((cx + 18.0 * np.cos(ang), cy + 18.0 * np.sin(ang)))

# 2. Medium Density Coordinates (5 clusters x 20 nodes = 100 clients + 1 Sink Node 1 = 101 motes)
coords_med = [(0.0, -160.0)]  # Dedicated RPL Root Sink Node 1 (Top Center, Visible)
med_hubs = [(-130.0, -80.0), (130.0, -80.0), (0.0, 30.0), (-130.0, 140.0), (130.0, 140.0)]
for h_idx, (cx, cy) in enumerate(med_hubs):
    if len(coords_med) >= 101: break
    coords_med.append((cx, cy))  # Cluster Head
    for i in range(19):
        if len(coords_med) >= 101: break
        ang = i * (2 * np.pi / 19.0)
        coords_med.append((cx + 32.0 * np.cos(ang), cy + 32.0 * np.sin(ang)))

# 3. High Density Coordinates (2 clusters x 50 nodes = 100 clients + 1 Sink Node 1 = 101 motes)
coords_high = [(0.0, -70.0)]  # Dedicated RPL Root Sink Node 1 (Top Center, Visible)
high_hubs = [(-110.0, 30.0), (110.0, 30.0)]
for h_idx, (cx, cy) in enumerate(high_hubs):
    if len(coords_high) >= 101: break
    coords_high.append((cx, cy))  # Cluster Head
    for i in range(49):
        if len(coords_high) >= 101: break
        ang = i * (2 * np.pi / 49.0)
        r_dist = 30.0 if i % 2 == 0 else 52.0
        coords_high.append((cx + r_dist * np.cos(ang), cy + r_dist * np.sin(ang)))

# 4. Lucas Adaptive Coordinates (Sequence 2, 1, 3, 4, 7, 11, 18, 29, 25 = 100 clients + 1 Sink Node 1 = 101 motes total)
coords_lucas = [(0.0, -200.0)]  # Dedicated RPL Root Sink Node 1 (Top Center, Visible)
lucas_sizes = [2, 1, 3, 4, 7, 11, 18, 29, 25]
lucas_hubs = [
    (-130.0, -130.0), (0.0, -130.0), (130.0, -130.0),
    (-130.0, 0.0), (0.0, 0.0), (130.0, 0.0),
    (-130.0, 130.0), (0.0, 130.0), (130.0, 130.0)
]
for idx, n_nodes in enumerate(lucas_sizes):
    if len(coords_lucas) >= 101: break
    cx, cy = lucas_hubs[idx]
    coords_lucas.append((cx, cy))  # Cluster Head
    r_radius = 18.0 + n_nodes * 1.0
    if n_nodes > 1:
        for i in range(n_nodes - 1):
            if len(coords_lucas) >= 101: break
            ang = i * (2 * np.pi / (n_nodes - 1))
            coords_lucas.append((cx + r_radius * np.cos(ang), cy + r_radius * np.sin(ang)))

generate_csc_file("lucas_low_density_100.csc", "Lucas Low Density 101 Motes (100 Clients + 1 Sink)", coords_low[:101])
generate_csc_file("lucas_medium_density_100.csc", "Lucas Medium Density 101 Motes (100 Clients + 1 Sink)", coords_med[:101])
generate_csc_file("lucas_high_density_100.csc", "Lucas High Density 101 Motes (100 Clients + 1 Sink)", coords_high[:101])
generate_csc_file("lucas_adaptive_lass_100.csc", "Lucas Adaptive LASS 101 Motes (100 Clients + 1 Sink)", coords_lucas[:101])

print("[+] All 4 Cooja Simulation .csc files updated with visible Sink Node 1 at top center!")
