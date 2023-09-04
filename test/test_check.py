import pytest
from app.api.connect import netmiko_connection, ncclient_connection
from .data_for_test import test_device
from app.api.create_loopback import create_loopback
from unittest.mock import Mock


## Test for connections
def test_connetion():
    pass
def test_disconnection():
    pass

## loopbacks
def test_connect_device():
    try:
        connection = netmiko_connection(test_device)
        assert connection is not None, "Failed to establish connection"
    except ConnectionError as e:
        assert False, str(e)
        

