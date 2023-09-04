from ncclient import manager

def connect():
    m = manager.connect(
        host='sandbox-iosxe-recomm-1.cisco.com',
        port='830',
        username='developer',
        password='lastorangerestoreball8876',
        timeout=10, 
        device_params={'name':'csr'},
        hostkey_verify=False)
    return m
