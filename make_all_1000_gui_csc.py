import os
import numpy as np

def generate_all_1000_deployments_native():
    num_motes = 1000
    deployments = ['lucas', 'hexagonal', 'grid', 'circular', 'random']
    coords = {}

    # 1. Lucas Coordinates
    clusters = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843]
    radii = [25.0, 45.0, 70.0, 100.0, 135.0, 175.0, 220.0, 270.0, 325.0, 390.0, 460.0, 540.0, 630.0, 730.0, 850.0]
    lx, ly = [0.0], [0.0]
    for c_idx, n in enumerate(clusters):
        if len(lx) >= num_motes: break
        rad = radii[c_idx]
        phase = c_idx * (137.508 * np.pi / 180.0)
        for a in np.linspace(0, 2 * np.pi, n, endpoint=False) + phase:
            if len(lx) >= num_motes: break
            lx.append(round(rad * np.cos(a), 2))
            ly.append(round(rad * np.sin(a), 2))
    coords['lucas'] = (lx[:num_motes], ly[:num_motes])

    # 2. Hexagonal Coordinates
    hx, hy = [0.0], [0.0]
    R = 35.0
    for ring in range(1, 40):
        if len(hx) >= num_motes: break
        for side in range(6):
            if len(hx) >= num_motes: break
            angle1 = side * np.pi / 3.0
            angle2 = (side + 1) * np.pi / 3.0
            for step in range(ring):
                if len(hx) >= num_motes: break
                t = step / ring
                hx.append(round(R * ring * ((1.0 - t) * np.cos(angle1) + t * np.cos(angle2)), 2))
                hy.append(round(R * ring * ((1.0 - t) * np.sin(angle1) + t * np.sin(angle2)), 2))
    coords['hexagonal'] = (hx[:num_motes], hy[:num_motes])

    # 3. Grid Coordinates
    gcoords = []
    side = int(np.ceil(np.sqrt(num_motes)))
    half = side // 2
    for row in range(-half, half + 2):
        for col in range(-half, half + 2):
            gcoords.append((round(col * 30.0, 2), round(row * 30.0, 2)))
    gcoords.sort(key=lambda p: p[0]**2 + p[1]**2)
    gcoords = gcoords[:num_motes]
    coords['grid'] = ([p[0] for p in gcoords], [p[1] for p in gcoords])

    # 4. Circular Coordinates
    cx, cy = [0.0], [0.0]
    c_rings = [8, 16, 24, 32, 45, 60, 80, 100, 160, 220, 300]
    c_radii = [40.0, 80.0, 120.0, 160.0, 210.0, 270.0, 340.0, 420.0, 520.0, 640.0, 780.0]
    for r_idx, n_nodes in enumerate(c_rings):
        r = c_radii[r_idx]
        for i in range(n_nodes):
            if len(cx) >= num_motes: break
            cx.append(round(r * np.cos(i * (2 * np.pi / n_nodes)), 2))
            cy.append(round(r * np.sin(i * (2 * np.pi / n_nodes)), 2))
    coords['circular'] = (cx[:num_motes], cy[:num_motes])

    # 5. Random Coordinates
    np.random.seed(42)
    rx = [0.0] + list(np.round(np.random.uniform(-400, 400, num_motes - 1), 2))
    ry = [0.0] + list(np.round(np.random.uniform(-400, 400, num_motes - 1), 2))
    coords['random'] = (rx[:num_motes], ry[:num_motes])

    output_files = []

    for top in deployments:
        x_pts, y_pts = coords[top]
        
        header = f"""<?xml version="1.0" encoding="UTF-8"?>
<simconf>
  <project EXPORT="discard">[APPS_DIR]/mrm</project>
  <project EXPORT="discard">[APPS_DIR]/mspsim</project>
  <simulation>
    <title>{top.capitalize()} 1000 Native Cooja Simulation</title>
    <randomseed>123456</randomseed>
    <motedelay_us>1000000</motedelay_us>
    <radiomedium>
      org.contikios.cooja.radiomediums.UDGM
      <transmitting_range>120.0</transmitting_range>
      <interference_range>240.0</interference_range>
      <success_ratio_tx>1.0</success_ratio_tx>
      <success_ratio_rx>1.0</success_ratio_rx>
    </radiomedium>
    <motetype>
      org.contikios.cooja.contikimote.ContikiMoteType
      <identifier>sink</identifier>
      <description>RPL Sink Server</description>
      <source EXPORT="discard">[CONTIKI_DIR]/examples/rpl-udp/udp-server.c</source>
      <commands EXPORT="discard">make TARGET=cooja udp-server.cooja</commands>
      <moteinterface>org.contikios.cooja.interfaces.Position</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.Battery</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiMoteID</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiRadio</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiButton</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiLED</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiClock</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiEEPROM</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiCFS</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiRS232</moteinterface>
    </motetype>
    <motetype>
      org.contikios.cooja.contikimote.ContikiMoteType
      <identifier>client</identifier>
      <description>RPL Client Node</description>
      <source EXPORT="discard">[CONTIKI_DIR]/examples/rpl-udp/udp-client.c</source>
      <commands EXPORT="discard">make TARGET=cooja udp-client.cooja</commands>
      <moteinterface>org.contikios.cooja.interfaces.Position</moteinterface>
      <moteinterface>org.contikios.cooja.interfaces.Battery</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiMoteID</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiRadio</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiButton</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiLED</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiClock</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiEEPROM</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiCFS</moteinterface>
      <moteinterface>org.contikios.cooja.contikimote.interfaces.ContikiRS232</moteinterface>
    </motetype>"""

        motes_xml = ""
        for i in range(num_motes):
            mtype = 'sink' if i == 0 else 'client'
            motes_xml += f"""
    <mote>
      <interface_config>
        org.contikios.cooja.interfaces.Position
        <x>{x_pts[i]}</x>
        <y>{y_pts[i]}</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        org.contikios.cooja.contikimote.interfaces.ContikiMoteID
        <id>{i+1}</id>
      </interface_config>
      <motetype_identifier>{mtype}</motetype_identifier>
    </mote>"""

        footer = """
  </simulation>
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
    <width>600</width>
    <z>2</z>
    <height>600</height>
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
    <width>1000</width>
    <z>3</z>
    <height>300</height>
    <location_x>400</location_x>
    <location_y>160</location_y>
  </plugin>
</simconf>"""

        filename = f"{top}1000_gui.csc"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, 'w') as f:
            f.write(header + motes_xml + footer)
        output_files.append(filename)
        print(f"[+] Generated Native 1000 Motes CSC: {filename}")

if __name__ == '__main__':
    generate_all_1000_deployments_native()
