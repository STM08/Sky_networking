# Imports
from netmiko import ConnectHandler
from devices import Device


# Connect using dictionary
# device = {
#     'ip' : "sandbox-iosxr-1.cisco.com",
#     'device-type' : "cisco_ios",
#     'username' : "admin",
#     'password' : "C1sco12345"
# }

# connection=netmiko.ConnectHandler(ip = device["ip"],
#                                   device_type = new_device["device_type"],
#                                   username = new_device["username"],
#                                   password = new_device["password)"]


new_device = Device("sandbox-iosxr-1.cisco.com", "cisco_ios", "admin",  "C1sco12345")


# Use ConnectHandler from netmiko, connect to a cisco device in sandbox
def connect_device(device):
    connection = ConnectHandler(ip = device.ip,
                                  device_type = device.device_type,
                                  username = device.username,
                                  password = device.password)
    return connection


# Print out the shell ip interface brief
# print(connect_device().send_command("sh ip int brief"))


# Loopback interface
def create_loopback(connection, loopback_number, ip_address):
    config_commands = [
        f"interface Loopback{loopback_number}",
        f"ip address {ip_address} 255.255.255.255",
        "no shutdown"
    ]
    output = connection.send_config_set(config_commands)
    return output

# Disconnect after printing
def disconnect_device():
    connect_device(new_device).disconnect()

if __name__ == "__main__":
    # Connect to the device
    connection = connect_device(new_device)

    # Create Loopback interface (Loopback1 with IP 10.0.0.1)
    output = create_loopback(connection, 1, "127.0.0.1")
    print("Configuration Output: ", output)

    # Disconnect from the device
    disconnect_device()


# disconnect_device()

# create_loopback()