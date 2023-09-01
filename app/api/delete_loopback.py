import xml.dom.minidom

def delete_loopback(connection):
        DELETE = """
        <config>
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                        <interface operation="delete">
                                <name>Loopback1</name>
                        </interface>
                </interfaces>
        </config>
        """

        RESPONSE = connection.edit_config(DELETE, target = 'running')
        RESPONSE = xml.dom.minidom.parseString(str(RESPONSE)).toprettyxml()

        return RESPONSE    