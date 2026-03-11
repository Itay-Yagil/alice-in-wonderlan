from firewall_rules.generic_rule import GenericRule
import scapy.all as s

class UDP(GenericRule):
    def is_relevant(self, packet):
        if s.UDP in packet:
            return True
        return False


class TCP(GenericRule):
    def is_relevant(self, packet):
        if s.TCP in packet:
            return True
        return False