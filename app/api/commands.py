# from api.connect import connect_device, disconnect_device

# from lxml import etree
from xml.dom.minidom import parseString
# Print out the ip interface brief
from api.netconf_connect import connect


def get_interface():
    connection = connect()
    print("connected")
    output = connection.get_config('running')
    print("2")
    xml_doc = parseString(output)
    print("3")
    print(xml_doc)
    connection.close_session()
    print("disconnected")
    return xml_doc

def get_loopback():
    connection = connect()
    print("connected")
    output = connection.get_config('running')
    xml_doc = parseString(str(output))
    loopback = xml_doc.getElementsByTagName("Loopback")
    print(loopback)
    connection.close_session()
    print("disconnected")
    print(xml_doc)
    return xml_doc

# # Create loopback interface
# def create_loopback(device, loopback_number, ip_address):
#     connection = connect_device(device)
#     config_commands = [
#         f"interface Loopback{loopback_number}",
#         f"ip address {ip_address} 255.255.255.255",
#         "no shutdown",
#         "commit",
#         "exit",
#         "exit",
#         "show ip int brief"
#     ]
#     connection.send_config_set(config_commands)
#     output = connection.send_command(f"show interfaces loopback {loopback_number}")
#     disconnect_device(connection)
#     return output

# # Delete loopback interface
# def delete_loopback(device, loopback_number):
#     connection = connect_device(device)
#     config_commands = [
#         f"no interface Loopback{loopback_number}",
#         "no shutdown",
#         "commit",
#         # "exit",
#         # "exit",
#         # "show ip int brief"
#     ]
#     connection.send_config_set(config_commands)
#     output = connection.send_command("sh ip int brief")
#     disconnect_device(connection)
#     return output
