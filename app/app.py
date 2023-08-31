import json

from flask import Flask, request
from api.commands import get_interface
from api.commands import create_loopback
from model.devices import Device

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello world from venv using Flask."
    
# @app.post("/connect")
# def connect():
#     input_json = request.get_json()
#     new_device = Device(input_json["ip"], input_json["device_type"], input_json["username"], input_json["password"])
#     try:
#         new_connection = connect_device(new_device)
#         return "Successfully connected!"
#     except:
#         return "Cannot retrieve interfaces"

@app.get("/interface")
def interface():
    input_json = request.get_json()
    new_device = Device(input_json["ip"], input_json["device_type"], input_json["username"], input_json["password"])
    try:
        output = get_interface(new_device)
        return output
    except:
        return "Cannot retrieve interfaces"
    
@app.post("/loopback")
def loopback():
    input_json = request.get_json()
    new_device = Device(input_json["ip"], input_json["device_type"], input_json["username"], input_json["password"])
    try:
        output = create_loopback(new_device, input_json["loopback_number"], input_json["loopback_ip_address"])
        print(output)
        return output
    except:
        return "Cannot create loopback"
