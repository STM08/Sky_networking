from ncclient import manager

def connect():
    RTR1_MGR = manager.connect(
        host='sandbox-iosxr-1.cisco.com',
        port='830',
        username='admin',
        password='C1sco12345',
        timeout=10, 
        device_params={'name':'csr'},
        hostkey_verify=False)
    return RTR1_MGR
