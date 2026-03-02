from firewall_rules.generic_rule import GenericRule
import scapy.all as s

class UdpPortRule(GenericRule):
    @classmethod
    def passes(cls, packet):
        if s.UDP in packet and (packet.dport == 12345 or packet.sport == 12345):
            return False
        return True