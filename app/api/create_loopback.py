import xml.dom.minidom

def create_loopback(connection, loopback):
    CONFIG = """
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                        <name>{name}</name>
                        <description>{description}</description>
                        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                        <enabled>true</enabled>
                        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                                <address>
                                        <ip>{ip}</ip>
                                        <netmask>{netmask}</netmask>
                                </address>
                        </ipv4>
                </interface>
        </interfaces>
    </config>
    """

    CONFIG = CONFIG.format(name=loopback["name"], description=loopback["description"], ip=loopback["ip"], netmask=loopback["netmask"])    
    RESPONSE = connection.edit_config(CONFIG, target = 'running')
    RESPONSE = xml.dom.minidom.parseString(str(RESPONSE)).toprettyxml()    

    return RESPONSE        