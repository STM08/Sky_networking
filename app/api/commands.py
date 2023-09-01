from api.netconf_connect import connect
from app.api.connect import connect_device, disconnect_device


def get_interface(device):
    connection = connect_device(device)
    output = connection.send_command("sh ip int brief")
    disconnect_device(connection)
    return output

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
