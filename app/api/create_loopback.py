import ncclient

from api.filter_loopback import filter_loopback

def create_loopback(m, request):
    loopback_config_template = """
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                        <name>Loopback{name}</name>
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
    if request["dry-run"] == False:   
        try:    
                m.edit_config(PAYLOAD, target = 'running')
                RESPONSE = filter_loopback(m, request["name"])
                print("SUCCESS")
                return "Successfully configured Loopback" + request["name"] + f"\n\n" + RESPONSE
        except ncclient.NCClientError as e:
                print("FAILED")
                return str(e)
    else:
         return "PAYLOAD:" + f"\n" + PAYLOAD 