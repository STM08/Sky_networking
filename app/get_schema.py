from ncclient import manager

RTR1_MGR = manager.connect(
        host='sandbox-iosxr-1.cisco.com',
        port='830',
        username='admin',
        password='C1sco12345',
        timeout=10, 
        device_params={'name':'csr'},
        hostkey_verify=False)

SCHEMA = RTR1_MGR.get_schema('ietf-interfaces')

print(SCHEMA)

RTR1_MGR.close_session()    