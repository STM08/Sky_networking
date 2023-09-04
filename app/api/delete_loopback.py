import xml.dom.minidom

def delete_loopback(m, request):
        DELETE = """
        <config>
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                        <interface operation="delete">
                                <name>{name}</name>
                        </interface>
                </interfaces>
        </config>
        """

        DELETE = DELETE.format(name=request["name"])

        RESPONSE = m.edit_config(DELETE, target = 'running')
        RESPONSE = xml.dom.minidom.parseString(str(RESPONSE)).toprettyxml()

        return RESPONSE    