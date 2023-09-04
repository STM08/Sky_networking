import xml.dom.minidom

def delete_loopback(connection, loopback):
        DELETE = """
        <config>
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                        <interface operation="delete">
                                <name>{name}</name>
                        </interface>
                </interfaces>
        </config>
        """

        DELETE = DELETE.format(name=loopback["name"])

        RESPONSE = connection.edit_config(DELETE, target = 'running')
        RESPONSE = xml.dom.minidom.parseString(str(RESPONSE)).toprettyxml()

        return RESPONSE    