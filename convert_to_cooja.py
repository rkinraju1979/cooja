import re, os

sink_motetype = '''    <motetype>
      org.contikios.cooja.contikimote.ContikiMoteType
      <identifier>sink</identifier>
      <description>RPL-UDP sink (server)</description>
      <source EXPORT="discard">/home/rkr/contiki-ng/examples/rpl-udp/udp-server.c</source>
      <commands EXPORT="discard">make TARGET=cooja udp-server.cooja</commands>
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
    </motetype>'''

client_motetype = '''    <motetype>
      org.contikios.cooja.contikimote.ContikiMoteType
      <identifier>client</identifier>
      <description>RPL-UDP client node</description>
      <source EXPORT="discard">/home/rkr/contiki-ng/examples/rpl-udp/udp-client.c</source>
      <commands EXPORT="discard">make TARGET=cooja udp-client.cooja</commands>
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
    </motetype>'''

# Cooja JS ScriptRunner plugin for 1000 rounds execution
js_script_plugin = '''  <plugin>
    org.contikios.cooja.plugins.ScriptRunner
    <plugin_config>
      <script>
TIMEOUT(10000000); // 1000 rounds * 10s = 10,000s simulation time (10,000,000 ms)

while (true) {
  log.log(time + " " + "NODE=" + id + " " + msg + "\\n");
  YIELD();
}
      </script>
      <active>true</active>
    </plugin_config>
    <width>600</width>
    <z>1</z>
    <height>700</height>
    <location_x>600</location_x>
    <location_y>0</location_y>
  </plugin>
'''

csc_files = ['circular29.csc', 'grid29.csc', 'hexagonal29.csc', 'lucas29.csc', 'random29.csc']
src_dir = '/mnt/c/Users/Kanaka Raju/Desktop/joy29'
dst_dir = '/home/rkr/simulations'

for fn in csc_files:
    src_path = os.path.join(src_dir, fn)
    with open(src_path, 'r') as f:
        content = f.read()
    
    # Replace motetypes using regex
    content = re.sub(r'<!-- Sink motetype -->\s*<motetype>.*?</motetype>', f'<!-- Sink motetype -->\n{sink_motetype}', content, flags=re.DOTALL)
    content = re.sub(r'<!-- Client motetype -->\s*<motetype>.*?</motetype>', f'<!-- Client motetype -->\n{client_motetype}', content, flags=re.DOTALL)
    content = re.sub(r'org\.contikios\.cooja\.mspmote\.interfaces\.MspMoteID', 'org.contikios.cooja.contikimote.interfaces.ContikiMoteID', content)
    
    # Inject ScriptRunner before </simconf>
    if 'org.contikios.cooja.plugins.ScriptRunner' not in content:
        content = content.replace('</simconf>', f'{js_script_plugin}\n</simconf>')
    
    dst_path = f'{dst_dir}/{fn}'
    with open(dst_path, 'w') as f:
        f.write(content)
    print(f'Converted {fn} -> {dst_path}')

print('CONVERSION_COMPLETE')
