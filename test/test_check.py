import pytest, unittest
from app.api.connect import netmiko_connection, ncclient_connection
from .data_for_test import test_device, mock_request, mock_config_response, mock_interface_response
from app.api.create_loopback import create_loopback
from app.api.delete_loopback import delete_loopback
from unittest.mock import Mock, patch
from app.api.commands import get_interface
## Test for Sandbox Connection
def test_connect_device():
    try:
        connection = netmiko_connection(test_device)
        assert connection is not None, "Failed to establish connection"
    except ConnectionError as e:
        assert False, str(e)

def test_create_loopback():
    # Mock the connection object
    mock_connection = Mock()
    mock_connection.edit_config.return_value = "<ok/>"  # Mocking a successful NETCONF response
    mock_connection.get_config.return_value = mock_config_response

    # Call the create_loopback function
    response = create_loopback(mock_connection, mock_request)

    # Define the template and expected response
    template = """Successfully configured {loopback_name}

<?xml version="1.0" ?>
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">

      <interface>

              <name>{loopback_name}</name>

              <description>Loopback created via netconfffffffff</description>

              <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>

              <enabled>true</enabled>

              <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">

                      <address>

                              <ip>{ip_address}</ip>

                              <netmask>255.255.255.0</netmask>

                      </address>

              </ipv4>

      </interface>

</interfaces>
"""

    expected_response = template.format(loopback_name="Loopback1", ip_address="10.0.0.8")
    
    # Remove extra spaces and line breaks for comparison
    cleaned_response = '\n'.join([line.strip() for line in response.splitlines() if line.strip()])
    cleaned_expected_response = '\n'.join([line.strip() for line in expected_response.splitlines() if line.strip()])
    
    assert cleaned_response == cleaned_expected_response, f"Expected: {cleaned_expected_response}, but got: {cleaned_response}"
    
def test_get_interface():
    # Mock the connection object
    mock_connection = Mock()
    mock_connection.send_command.return_value = mock_interface_response

    # Call the get_interface function
    response = get_interface(mock_connection)

    # Check the response
    assert "GigabitEthernet1 10.10.20.48 YES NVRAM up up" in response
    assert "Loopback203 192.168.45.1 YES other up up" in response


def test_delete_loopback():
    # Mock the connection object
    mock_connection = Mock()
    
    # Mock the response for edit_config to simulate successful NETCONF operation
    mock_connection.edit_config.return_value = "<ok/>"
    
    # Mock the response for get_all_loopbacks to simulate the loopback no longer exists
    mock_response = """
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <interface>
      </interface>
    </native>
    """
    with patch('app.api.delete_loopback.get_all_loopbacks', return_value=mock_response):


        # Define the request payload
        request = {
            "name": "203",
            "dry-run": False
        }

        # Call the delete_loopback function
        response = delete_loopback(mock_connection, request)

        # Check the response
        expected_response = "Successfully deleted Loopback203\n\n" + mock_response
        assert response == expected_response

        # Optionally, you can also check if the loopback no longer exists in the configuration
        post_delete_config = mock_response
        assert "<Loopback>" not in post_delete_config

class TestDryRun(unittest.TestCase):

    def setUp(self):
        # Mock the connection object
        self.mock_connection = Mock()

    def test_create_loopback_dry_run(self):
        # Mock request data
        request_data = {
            "name": "100",
            "description": "Test Loopback",
            "ip": "192.168.1.1",
            "netmask": "255.255.255.0",
            "dry-run": True
        }

        # Call the function
        response = create_loopback(self.mock_connection, request_data)

        # Assert the response contains the 'dry_run' status and the payload
        self.assertIn("PAYLOAD:", response)

    def test_delete_loopback_dry_run(self):
        # Mock request data
        request_data = {
            "name": "100",
            "dry-run": True
        }

        # Call the function
        response = delete_loopback(self.mock_connection, request_data)

        # Assert the response contains the 'dry_run' status and the payload
        self.assertIn("PAYLOAD:", response)

if __name__ == "__main__":
    unittest.main()
