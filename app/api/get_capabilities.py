from ncclient import manager

from netconf_connect import connect


RTR1_MGR = connect()

for RTR_Capability in RTR1_MGR.server_capabilities:
    print(RTR_Capability)

RTR1_MGR.close_session()    