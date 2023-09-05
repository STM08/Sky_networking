class MockDevice:
    def __init__(self, ip, device_type, username, password):
        self.ip = ip
        self.device_type = device_type
        self.username = username
        self.password = password

test_device = MockDevice(
    ip="sandbox-iosxe-recomm-1.cisco.com",
    device_type="cisco_ios",
    username="developer",
    password="lastorangerestoreball8876"
)

mock_request = {
    "name": "1",
    "description": "Loopback created via netconfffffffff",
    "ip": "10.0.0.8",
    "netmask": "255.255.255.0",
    "dry-run": False
}
mock_interface_response = """
Interface IP-Address OK? Method Status Protocol
GigabitEthernet1 10.10.20.48 YES NVRAM up up
GigabitEthernet2 unassigned YES NVRAM administratively down down
GigabitEthernet3 unassigned YES NVRAM administratively down down
Loopback203 192.168.45.1 YES other up up
"""

mock_config_response = """<?xml version="1.0" ?>
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
        <name>Loopback1</name>
        <description>Loopback created via netconfffffffff</description>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
        <enabled>true</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
            <address>
                <ip>10.0.0.8</ip>
                <netmask>255.255.255.0</netmask>
            </address>
        </ipv4>
    </interface>
</interfaces>
"""


