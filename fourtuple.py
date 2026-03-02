class Fourtuple:
    def __init__(self, client_ip, client_port, server_ip, server_port):
        self.client_ip = client_ip
        self.client_port = client_port
        self.server_ip = server_ip
        self.server_port = server_port
    
    def __eq__(self, value):
        if type(value) is not Fourtuple:
            return False
        if value.client_ip != self.client_ip or value.client_port != self.client_port or \
           value.server_ip != self.server_ip or value.server_port != self.server_port:
            return False
        return True