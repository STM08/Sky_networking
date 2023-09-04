import xml.dom.minidom

def filter_loopback(m, loopback_name):
  loopback_filter_template = """
  <filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <interface>
        <Loopback>
          <name>{name}</name>
        </Loopback>
      </interface>
    </native>
  </filter>
  """

  PAYLOAD = loopback_filter_template.format(name=loopback_name)
  RESPONSE = m.get_config('running', PAYLOAD)
  RESPONSE = xml.dom.minidom.parseString(str(RESPONSE)).toprettyxml()

  return RESPONSE
      