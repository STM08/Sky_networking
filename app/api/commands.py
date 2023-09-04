def get_interface(m):
    output = m.send_command("sh clock") + f"\n\n" + m.send_command("sh ip int brief")
    return output
