import re

desktop_lucas = 'c:/Users/Kanaka Raju/Desktop/joy29/lucas29.csc'

with open(desktop_lucas, 'r') as f:
    content = f.read()

# Replace sky1 motetype definition with RPL-UDP sink and client motetypes
old_motetype_pattern = r'<motetype>.*?org\.contikios\.cooja\.mspmote\.SkyMoteType.*?</motetype>'

new_motetypes = """<!-- Sink motetype -->
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

content = re.sub(old_motetype_pattern, new_motetypes, content, flags=re.DOTALL)

# Update node 1 to sink and nodes 2-29 to client
mote_blocks = content.split('<mote>')
new_blocks = [mote_blocks[0]]

for block in mote_blocks[1:]:
    id_match = re.search(r'<id>([0-9]+)</id>', block)
    m_id = int(id_match.group(1)) if id_match else 0
    
    if m_id == 1:
        block = re.sub(r'<motetype_identifier>.*?</motetype_identifier>', '<motetype_identifier>sink</motetype_identifier>', block)
    else:
        block = re.sub(r'<motetype_identifier>.*?</motetype_identifier>', '<motetype_identifier>client</motetype_identifier>', block)
    new_blocks.append(block)

fixed_content = '<mote>'.join(new_blocks)

with open(desktop_lucas, 'w') as f:
    f.write(fixed_content)

print("[+] Successfully fixed lucas29.csc motetypes and C source paths!")
