
from flask import Flask, request
from api.commands import get_interface
from api.connect import netmiko_connection, ncclient_connection
from api.create_loopback import create_loopback
from api.delete_loopback import delete_loopback

from model.devices import Device

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world from venv using Flask."
    
@app.get("/interface")
def interface():
    input_json = request.get_json()
    device = Device(input_json["ip"], input_json["device_type"], input_json["username"], input_json["password"])
    m = netmiko_connection(device)
    try:
        output = get_interface(m)
        m.disconnect()
        return output
    except Exception as e:
        print(e)
        return "Unable to get interface"
    
@app.post("/loopback")
def add_loopback():
    input_json = request.get_json()
    m = ncclient_connection(input_json)
    print("Connected")
    try:
        RESPONSE = create_loopback(m, input_json)
        m.close_session()
        print("Disconnected")
        return RESPONSE
    except Exception as e:
        print(e)
        return "Unable to configure loopback"
    
@app.delete("/loopback")
def remove_loopback():
    input_json = request.get_json()
    m = ncclient_connection(input_json)
    print("Connected")
    try:
        RESPONSE = delete_loopback(m, input_json)
        m.close_session()
        print("Disconnected")
        return RESPONSE 
    except Exception as e:
        print(e)
        return "Unable to delete loopback"
