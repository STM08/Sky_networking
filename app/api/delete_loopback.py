from ncclient import manager
# import xml.dom.minidom

from netconf_connect import connect

DELETE = """
<config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface operation="delete">
                        <name>Loopback1</name>
                </interface>
        </interfaces>
</config>
"""

RTR1_MGR = connect()

# PAYLOAD = CONFIG(int_name = "Loopback1", int_desc = "Loopback created via netconf", ip_address = "10.0.0.6" )

RESPONSE = RTR1_MGR.edit_config(DELETE, target = 'running')

print(RESPONSE)

RTR1_MGR.close_session()    