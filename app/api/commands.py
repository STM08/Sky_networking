def get_interface(connection):
    output = connection.send_command("sh ip int brief")
    return output
