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
        #return e
        raise ConnectionError(f"Failed to connect: {e}")
def ncclient_connection():
    m = manager.connect(
        host='sandbox-iosxe-recomm-1.cisco.com',
        port='830',
        username='developer',
        password='lastorangerestoreball8876',
        timeout=10, 
        device_params={'name':'csr'},
        hostkey_verify=False)
    return m