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
