import xml.dom.minidom

def get_all_loopbacks(m):
  loopback_filter = """
  <filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <interface>
        <Loopback>
        </Loopback>
      </interface>
    </native>
  </filter>
  """

  PAYLOAD = loopback_filter
  RESPONSE = m.get_config('running', PAYLOAD)
  RESPONSE = xml.dom.minidom.parseString(str(RESPONSE)).toprettyxml()

  return RESPONSE
      