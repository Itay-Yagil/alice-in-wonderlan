import ipaddress

class Entry:
    def __init__(self, inteface, subnet):
        self._inteface = inteface
        self._subnet = ipaddress.ip_network(subnet)
    
    def is_match(self, ip):
        return ipaddress.ip_address(ip) in self._subnet
    
    def get_interface_name(self):
        return self._inteface.name


class RoutingTable:
    def __init__(self, entries = []):
        self.table = entries
    
    def add_entry(self, entry, index = 0):
        self.table.insert(index, entry)
    
    def remove_entry(self, index):
        del self.table[index]

    def find_match(self, ip):
        for entry in self.table:
            if entry.is_match(ip):
                return entry
        return None