from firewall_rules.generic_rule import GenericRule
import scapy.all as s

class Port(GenericRule):
    def __init__(self, port):
        self.port = port

    def is_relevant(self, packet):
        if (s.UDP in packet or s.TCP in packet) and (packet.sport == self.port or packet.dport == self.port):
            return True
        return False