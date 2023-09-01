from ncclient import manager
# import xmltodict
import xml.dom.minidom

from netconf_connect import connect

RTR1_MGR = connect()

CONFIG = RTR1_MGR.get_config('running')

print(xml.dom.minidom.parseString(str(CONFIG)).toprettyxml())

RTR1_MGR.close_session()    