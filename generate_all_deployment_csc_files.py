import os
import numpy as np

base_dir = os.path.dirname(os.path.abspath(__file__))

scales = [29, 47, 76, 123, 199]
deployments = ['lucas', 'hexagonal', 'grid', 'circular', 'random']

print("=== GENERATING ALL 25 COOJA (.csc) XML SIMULATION FILES WITH VISUALIZER PLUGINS ===")

def get_coordinates(top, num_motes):
    if top == 'lucas':
        clusters = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123]
        radii = [25.0, 45.0, 70.0, 100.0, 135.0, 175.0, 220.0, 270.0, 325.0, 390.0, 460.0]
        lx, ly = [0.0], [0.0]
        for c_idx, n in enumerate(clusters):
            if len(lx) >= num_motes: break
            rad = radii[c_idx]
            phase = c_idx * (137.508 * np.pi / 180.0)
            for a in np.linspace(0, 2 * np.pi, n, endpoint=False) + phase:
                if len(lx) >= num_motes: break
                lx.append(round(rad * np.cos(a), 2))
                ly.append(round(rad * np.sin(a), 2))
        return list(zip(lx[:num_motes], ly[:num_motes]))

    elif top == 'hexagonal':
        hx, hy = [0.0], [0.0]
        R = 35.0
        for ring in range(1, 15):
            if len(hx) >= num_motes: break
            for side in range(6):
                if len(hx) >= num_motes: break
                angle1 = side * np.pi / 3.0
                angle2 = (side + 1) * np.pi / 3.0
                for step in range(ring):
                    if len(hx) >= num_motes: break
                    t = step / ring
                    x = R * ring * ((1.0 - t) * np.cos(angle1) + t * np.cos(angle2))
                    y = R * ring * ((1.0 - t) * np.sin(angle1) + t * np.sin(angle2))
                    hx.append(round(x, 2))
                    hy.append(round(y, 2))
        return list(zip(hx[:num_motes], hy[:num_motes]))

    elif top == 'grid':
        gcoords = []
        side = int(np.ceil(np.sqrt(num_motes)))
        half = side // 2
        for row in range(-half, half + 2):
            for col in range(-half, half + 2):
                gcoords.append((round(col * 30.0, 2), round(row * 30.0, 2)))
        gcoords.sort(key=lambda p: p[0]**2 + p[1]**2)
        return gcoords[:num_motes]

    elif top == 'circular':
        cx, cy = [0.0], [0.0]
        c_rings = [8, 16, 24, 32, 45, 60, 80]
        c_radii = [40.0, 80.0, 120.0, 160.0, 210.0, 270.0, 340.0]
        for r_idx, n_nodes in enumerate(c_rings):
            r = c_radii[r_idx]
            for i in range(n_nodes):
                if len(cx) >= num_motes: break
                angle = i * (2 * np.pi / n_nodes)
                cx.append(round(r * np.cos(angle), 2))
                cy.append(round(r * np.sin(angle), 2))
        return list(zip(cx[:num_motes], cy[:num_motes]))

    elif top == 'random':
        np.random.seed(42 + num_motes)
        rx = [0.0] + list(np.round(np.random.uniform(-220, 220, num_motes - 1), 2))
        ry = [0.0] + list(np.round(np.random.uniform(-220, 220, num_motes - 1), 2))
        return list(zip(rx[:num_motes], ry[:num_motes]))

def generate_csc_xml(top_name, num_motes, coords):
    csc_filename = f"{top_name}{num_motes}.csc"
    csc_filepath = os.path.join(base_dir, csc_filename)

    xml_parts = [
        f"""<?xml version='1.0' encoding='UTF-8'?>
<simconf>
  <project EXPORT="discard">[APPS_DIR]/mrm</project>
  <project EXPORT="discard">[APPS_DIR]/mspsim</project>
  <project EXPORT="discard">[APPS_DIR]/avrora</project>
  <project EXPORT="discard">[APPS_DIR]/serial_socket</project>
  <project EXPORT="discard">[APPS_DIR]/collect-view</project>
  <project EXPORT="discard">[APPS_DIR]/powertracker</project>
  <simulation>
    <title>{top_name.capitalize()} {num_motes}-Mote RPL-UDP Simulation</title>
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

    for i, (x, y) in enumerate(coords):
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

    # Standard Cooja GUI Plugin Blocks (Visualizer Network Window, SimControl, LogListener)
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

    with open(csc_filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_parts))
    print(f"[+] Created Cooja XML with Visualizer: {csc_filename}")

count = 0
for m in scales:
    for top in deployments:
        c = get_coordinates(top, m)
        generate_csc_xml(top, m, c)
        count += 1

print(f"[+] SUCCESS: Generated ALL {count} Cooja XML Simulation Files with Network Visualizer Window Plugins!")
