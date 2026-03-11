from firewall_rules.generic_rule import GenericRule
import scapy.all as s

class SrcIP(GenericRule):
    def __init__(self, ip):
        self.ip = ip

    def is_relevant(self, packet):
        if s.IP in packet and packet[s.IP].src == self.ip:
            return True
        return False


class DstIP(GenericRule):
    def __init__(self, ip):
        self.ip = ip

    def is_relevant(self, packet):
        if s.IP in packet and packet[s.IP].dst == self.ip:
            return True
        return False