import xml.dom.minidom

def create_loopback(connection):
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

    RESPONSE = connection.edit_config(CONFIG, target = 'running')
    RESPONSE = xml.dom.minidom.parseString(str(RESPONSE)).toprettyxml()    

    return RESPONSE        