from ncclient import manager
# import xml.dom.minidom

from netconf_connect import connect

CONFIG = """
<config>
     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
             <interface>
                     <name>Loopback1</name>
                     <description>Loopback created via netconfffffffff</description>
                     <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                     <enabled>true</enabled>
                     <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                             <address>
                                     <ip>10.0.0.8</ip>
                                     <netmask>255.255.255.0</netmask>
                             </address>
                     </ipv4>
             </interface>
     </interfaces>
</config>
"""

RTR1_MGR = connect()

# PAYLOAD = CONFIG(int_name = "Loopback1", int_desc = "Loopback created via netconf", ip_address = "10.0.0.6" )

RESPONSE = RTR1_MGR.edit_config(CONFIG, target = 'running')

print(RESPONSE)

RTR1_MGR.close_session()    