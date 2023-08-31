from netmiko import ConnectHandler
from model.devices import Device

def connect_device(device):
    try:
        connection=ConnectHandler(ip = device.ip,
                                  device_type = device.device_type,
                                  username = device.username,
                                  password = device.password)
        print("Successfully connected!")
        return connection
    except:
        return ConnectionRefusedError

def disconnect_device(connection):
    try:
         connection.disconnect()
         print("Successfully disconnected!")
    except:
        print("Cannot disconnect!")
