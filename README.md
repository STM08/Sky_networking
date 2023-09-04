# Sky_networking
#### Overview

The Sky_networking repository contains a Python-based network automation program that interacts with network devices using both NETCONF (via ncclient) and CLI (via netmiko). The program provides a Flask-based REST API to perform various operations on the network devices.

#### Installation (Windows / MacOS)
Prerequisites
- Python 3.x
- git (for cloning the repository)
- Postman (for testing the API)
##### MacOS

- git clone this repository
- run this code in terminal, `source .venv/bin/activate` , to create a virtual environment.
- Install Flask, `python -m pip install flask`
- Install netmiko : ` pip install netmiko`
- install ncclient: ` pip install ncclient`
  
#### Running the Code

To run the main application, execute the app.py script:

python app.py


This will start the Flask web application, and you can access it via a web browser at http://127.0.0.1:5000/.
