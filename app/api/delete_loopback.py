import ncclient

from .get_all_loopbacks import get_all_loopbacks

def delete_loopback(m, request):
        delete_loopback_template = """
        <config>
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                        <interface operation="delete">
                                <name>Loopback{name}</name>
                        </interface>
                </interfaces>
        </config>
        """

        PAYLOAD = delete_loopback_template.format(name=request["name"])
        if request["dry-run"] == False:
           try:
                m.edit_config(PAYLOAD, target = 'running')
                RESPONSE = get_all_loopbacks(m)
                print("SUCCESS")
                return "Successfully deleted Loopback" + request["name"] + f"\n\n" + RESPONSE
           except ncclient.NCClientError as e:
                print("FAIL")
                raise Exception(e)
        else:
             return "PAYLOAD:" + f"\n" + PAYLOAD
        

