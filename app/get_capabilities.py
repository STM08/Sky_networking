from ncclient import manager

RTR1_MGR = manager.connect(
        host='sandbox-iosxr-1.cisco.com',
        port='830',
        username='admin',
        password='C1sco12345',
        timeout=10, 
        device_params={'name':'csr'},
        hostkey_verify=False)

for RTR_Capability in RTR1_MGR.server_capabilities:
    print(RTR_Capability)

RTR1_MGR.close_session()    