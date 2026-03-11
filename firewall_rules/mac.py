from firewall_rules.generic_rule import GenericRule
import scapy.all as s

class SrcMAC(GenericRule):
    def __init__(self, mac):
        self.mac = mac

    def is_relevant(self, packet):
        if s.Ether in packet and packet.src == self.mac:
            return True
        return False


class DstMAC(GenericRule):
    def __init__(self, mac):
        self.mac = mac

    def is_relevant(self, packet):
        if s.Ether in packet and packet.dst == self.mac:
            return True
        return False