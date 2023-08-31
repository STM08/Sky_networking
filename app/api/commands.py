from api.connect import connect_device, disconnect_device

# Print out the ip interface brief
def get_interface(device):
    connection = connect_device(device)
    output = connection.send_command("sh ip int brief")
    disconnect_device(connection)
    return output

# Loopback interface
def create_loopback(device, loopback_number, ip_address):
    connection = connect_device(device)
    config_commands = [
        f"interface Loopback{loopback_number}",
        f"ip address {ip_address} 255.255.255.255",
        "no shutdown",
        "commit",
        "exit",
        "exit",
        "show ip int brief"
    ]

    output = connection.send_config_set(config_commands)
    disconnect_device(connection)
    return output