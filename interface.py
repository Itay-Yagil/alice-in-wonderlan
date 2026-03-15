import scapy.all as s

class Interface:
    def __init__(self, name, mac, ip, subnet):
        self._name = name
        self._mac = mac
        self._ip = ip
        self._subnet = subnet
    
    def get_name(self):
        return self._name
    
    def get_mac(self):
        return self._mac
    
    def get_ip(self):
        return self._ip
    
    def get_subnet(self):
        return self._subnet