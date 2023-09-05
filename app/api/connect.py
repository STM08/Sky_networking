from netmiko import ConnectHandler
from ncclient import manager

def netmiko_connection(device):
    try:
        m = ConnectHandler(ip = device.ip,
                                  device_type = device.device_type,
                                  username = device.username,
                                  password = device.password)
        print("Successfully connected")
        return m
    except Exception as e:
        return e
    
def ncclient_connection(device):
    try:
        m = manager.connect(
            host=device["host"],
            port=device["port"],
            username=device["username"],
            password=device["password"],
            timeout=10, 
            device_params={'name':'csr'},
            hostkey_verify=False)
        return m
    except Exception as e:
        return e