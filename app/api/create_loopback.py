import xml.dom.minidom

def create_loopback(m, request):
    loopback_config_template = """
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

    PAYLOAD = loopback_config_template.format(name=request["name"], description=request["description"], ip=request["ip"], netmask=request["netmask"])  

    try:    
        RESPONSE = m.edit_config(PAYLOAD, target = 'running')
        RESPONSE = xml.dom.minidom.parseString(str(RESPONSE)).toprettyxml()
        return RESPONSE
    except:
        return "Failed to create loopback"