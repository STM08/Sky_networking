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
def connect_device():
    connection=ConnectHandler(ip = new_device.ip,
                                  device_type = new_device.device_type,
                                  username = new_device.username,
                                  password = new_device.password)

    return connection

# Print out the shell ip interface brief
print(connect_device().send_command("sh ip int brief"))


# Disconnect after printing
def disconnect_device():
    connect_device().disconnect()

disconnect_device()