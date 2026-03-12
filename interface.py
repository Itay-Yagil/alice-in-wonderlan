import ipaddress

class Interface:
    def __init__(self, name, ip, mac):
        self._name = name
        self._ip = ip
        self._mac = mac

    def get_name(self):
        return self._name
    
    def get_mac(self):
        return self._mac
    
    def get_ip(self):
        return self._ip
    