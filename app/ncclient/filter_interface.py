import xml.dom.minidom

from netconf_connect import connect

RTR1_MGR = connect()

FILTER = """
  <filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
   <interface></interface>
  </native>
 </filter>
"""

CONFIG = RTR1_MGR.get_config('running', FILTER)

print(xml.dom.minidom.parseString(str(CONFIG)).toprettyxml())

RTR1_MGR.close_session()    