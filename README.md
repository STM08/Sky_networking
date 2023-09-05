# Sky_networking

## Overview

The Sky_networking repository contains a Python-based network automation program that interacts with network devices using both NETCONF (via ncclient) and CLI (via netmiko). The program provides a Flask-based REST API to perform various operations on the network devices.

### Built with :

- Python
- Flask
- netconf
- netmiko
- pytest
- Cisco CSR1000V, Always-on Cisco router via Cisco sandbox, [explained here](https://www.cisco.com/c/en/us/products/routers/cloud-services-router-1000v-series/index.html)
- [Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology) (Need an account)

---

## Getting Started

- ### Installation

  - **Prerequisites**

    - Python 3.x
    - git (for cloning the repository)
    - Postman (for testing the API)

  - ### Windows

    - Git clone this repository
    - Run this code in terminal, `.venv\Scripts\Activate.ps1`, to create a virtual environment.
    - Install required libraries: `pip install -r requirements.txt`

  - ### MacOS

    - Git clone this repository
    - Run this code in terminal, `source .venv/bin/activate` , to create a virtual environment.
    - Install required libraries: `pip install -r requirements.txt`

- ### Running the Code

  - ### Routes

    - In the terminal, make sure you are in the folder that contains `app.py`.
    - To start the flask application, run the following command: `python -m flask run`

      This will start the Flask web application, and you can access it via a web browser at http://127.0.0.1:5000/

    - Once connected, the terminal should display:

          WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
          Running on http://127.0.0.1:5000
          Press CTRL+C to quit

  - ### Making requests to the Application

    - You can use POSTMAN to make a **GET** / **POST** / **DELETE** request.
    - By default, the `dry-run` is set to false, which sends the PAYLOAD to the device and a configured loopback in XML format is sent to the user.
    - It can be set to _true_ to only send the PAYLOAD to the user, to examine the configuration.

      - **GET** :

        - `/interface`

        Example body format to get an interface of a specific device:

        ```
        {

            "ip": "sandbox-iosxe-recomm-1.cisco.com",

            "device_type": "cisco_ios",

            "username": "developer",

            "password": "lastorangerestoreball8876"

        }
        ```

      - **POST**:

        - `/loopback`

        Example body format to create a loopback:

        ```
        {
            "host": "sandbox-iosxe-recomm-1.cisco.com",

            "port": "830",

            "username": "developer",

            "password": "lastorangerestoreball8876",

            "name": "4",

            "description": "TEST",

            "ip": "10.0.0.10",

            "netmask": "255.255.255.0",

            "dry-run": false

        }
        ```

      - **DELETE**:

        - `/loopback`

        Example body format to delete a loopback:

        ```
        {

            "host": "sandbox-iosxe-recomm-1.cisco.com",

            "port": "830",

            "username": "developer",

            "password": "lastorangerestoreball8876",

            "name":"3",

            "dry-run":false
        }
        ```

- ### Running the TESTS

  - Install pytest `pip install pytest`
  - Run the test `pytest`

- ### Project Folder structure

```

├── app
│ ├── api
│ │ ├── **init.py**
│ │ ├── create_loopback.py
│ │ ├── delete_loopback.py
│ │ └── ... (other API related files)
│ ├── model
│ │ └── **init.py**
│ │ └── devices.py
│ │ └── ... (model related files)
│ └── **init.py**
│ └── app.py
│ └── requirements.txt
└── test
├── test_check.py
└── ... (other test files)

```

There are two main folders, _app_ and _test_ respectively.

Inside the _app_ folder, it contains 2 subfolders, _api_ and _model_ and a main _app.py_ file. The api folder contains files that connects to the devices via netconf and netmiko.

---

## Problem Statements

- ### Overview

  We were required to apply our knowledge from the Cisco Networking Academy to the real (virtual) world. By connecting to a cisco router via netconf, viewing the interface brief which displays all the connected devices, then progressing by creating and deleting loopbacks dynamically.

  One of the first hurdles we faced as a team was connecting to the device. We used netmiko initially to connect to the device and overcome most of our product backlog such as creating and deleting a loopback, viewing the interface to see all the connected devices. This conflicted with the requirements as netconf was the preferred way to connect.

- ### User stories

  We started off by planning the whole project before jumping into coding. By creating user EPICS, we then dissected each epic to multiple user stories. This allowed us to create product backlogs to complete the requirements.

  As a group, we gave each task a story point between 1 - 13, higher the number, the more difficult the task is. Using [**Planning Poker**](https://planningpokeronline.com/) for each backlog to determine the difficulty in completing the task in hand, we took into consideration of the time and complexity of the code to decide the number for the task.

  Some user epics were:

        As a network engineer , I want to remotely connect with a network device for the program so that I can interact with it.

        As a network engineer, I would like to configure testing tools, so that I can diagnose network issues.

  Some user stories were:

        As a network engineer, I would like to connect to a device, so that I can communicate with it and see it's properties.

        As a network engineer, I would like to send and receive a loopback from a device, so that I can see if it connected to the network.

        As a network engineer, I would like to display a list of device interface, so that I can see their statuses.

- ### Domain Model

  | Object | Attributes  | Action                | Return          |
  | ------ | ----------- | --------------------- | --------------- |
  | Device | ip          | netmiko_connection()  | netmiko object  |
  |        | device_type | ncclient_connection() | ncclient object |
  |        | username    | delete_loopback()     | XML             |
  |        | password    | create_loopback()     | XML             |
  |        |             | filter_loopback()     | XML             |
  |        |             | get_all_loopbacks()   | XML             |
  |        |             | get_interface()       | String          |

- ### Tests

  The tests files can be found under _test_ folder. It consists of 3 files, `__init.py__` , `data_for_test.py`, `test_check.py`.

  `__init.py__` is used to mark a directory as a Python package, it can be left empty.

  `data_for_test.py` contains the mock data that will test the actual connection with the sandbox.

  `test_check.py` contains 2 unit tests, one to test for the connection to the sandbox, another one for the correct XML configuration when creating a loopback.

## Project Review and Roadmap
