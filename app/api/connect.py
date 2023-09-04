from netmiko import ConnectHandler

def connect_device(device):
    try:
        m = ConnectHandler(ip = device.ip,
                                  device_type = device.device_type,
                                  username = device.username,
                                  password = device.password)
        print("Successfully connected!")
        return m
    except:
        return ConnectionRefusedError

def disconnect_device(m):
    try:
         m.disconnect()
         print("Successfully disconnected!")
    except:
        print("Cannot disconnect!")
