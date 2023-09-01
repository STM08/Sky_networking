from ncclient import manager
# import xmltodict
import xml.dom.minidom

from netconf_connect import connect

RTR1_MGR = connect()

SCHEMA = RTR1_MGR.get_schema('ietf-interfaces')

print(xml.dom.minidom.parseString(str(SCHEMA)).toprettyxml())

RTR1_MGR.close_session()    