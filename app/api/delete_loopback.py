import xml.dom.minidom

def delete_loopback(m, request):
        delete_loopback_template = """
        <config>
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                        <interface operation="delete">
                                <name>{name}</name>
                        </interface>
                </interfaces>
        </config>
        """

        PAYLOAD = delete_loopback_template.format(name=request["name"])

        try:
            RESPONSE = m.edit_config(PAYLOAD, target = 'running')
            RESPONSE = xml.dom.minidom.parseString(str(RESPONSE)).toprettyxml()
            return RESPONSE
        except:
            return "Failed to delete loopback"    

