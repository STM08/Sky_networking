
from flask import Flask, request
from api.commands import get_interface
from api.netconf_connect import connect
from api.connect import connect_device
from api.connect import disconnect_device
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
    m = connect_device(device)
    try:
        output = get_interface(m)
        disconnect_device(m)
        return output
    except:
        return "Cannot retrieve interfaces"
    
@app.post("/loopback")
def add_loopback():
    m = connect()
    print("Connected")
    try:
        input_json = request.get_json()
        RESPONSE = create_loopback(m, input_json)
        m.close_session()
        print("Disconnected")
        return RESPONSE
    except:
        return "Cannot create loopbacks"
    
@app.delete("/loopback")
def remove_loopback():
    m = connect()
    input_json = request.get_json()
    try:
        print("Try")
        RESPONSE = delete_loopback(m, input_json)
        m.close_session()
        print("Disconnected")
        print(RESPONSE)
        return "Loopback removed" 
    except:
        return "Cannot delete loopback"
