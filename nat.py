import scapy.all as s
from nat_sessions import NatSessions
from fourtuple import Fourtuple
from firewall import Firewall

class Nat:
    def __init__(self, in_iface, out_iface):
        self.sessions = NatSessions()
        self.firewall = Firewall()
        self.in_iface = in_iface
        self.out_iface = out_iface
        self.in_sock = s.conf.L2socket(self.in_iface.name)
        self.out_sock = s.conf.L2socket(self.out_iface.name)

    def run(self):
        while True:
            packet = s.sniff(iface=[self.in_iface.name, self.out_iface.name], count=1)[0]
            sniffed_iface_name = packet.sniffed_on
            if not self.firewall.check(packet):
                print("Packed dropped")
                packet.show()
            elif sniffed_iface_name == self.in_iface.name:
                print(f"Sniffed on {self.in_iface.name}")
                packet.show()
                self._to_out_nat(packet)
                print(self.sessions)
            elif sniffed_iface_name == self.out_iface.name:
                print(f"Sniffed on {self.out_iface.name}")
                packet.show()
                self._to_in_nat(packet)
                print(self.sessions)

    def _to_out_nat(self, packet):
        if not is_layer_four_packet(packet):
             return False
        src_fourtuple = Fourtuple(packet[s.IP].src, packet.sport, packet[s.IP].dst, packet.dport)
        self._verify_session(src_fourtuple)
        packet.src = self.out_iface.mac
        nat_fourtuple = self.sessions.get_nat_fourtuple(src_fourtuple)
        self._change_packet_fourtuple(packet, nat_fourtuple.client_ip, nat_fourtuple.client_port, \
                                      nat_fourtuple.server_ip, nat_fourtuple.server_port)
        self.out_sock.send(packet)
        print(f"SENT OUT")
        packet.show()
        return True

    def _to_in_nat(self, packet):
        if not is_layer_four_packet(packet):
            return False
        nat_fourtuple = Fourtuple(packet[s.IP].dst, packet.dport, packet[s.IP].src, packet.sport)
        if not self.sessions.is_nat_session_exists(nat_fourtuple):
            return False
        packet.dst = self.in_iface.mac
        src_fourtuple = self.sessions.get_src_fourtuple(nat_fourtuple)
        self._change_packet_fourtuple(packet, src_fourtuple.server_ip, src_fourtuple.server_port, \
                                      src_fourtuple.client_ip, src_fourtuple.client_port)
        self.in_sock.send(packet)
        print(f"SENT IN")
        packet.show()
        return True

    def _change_packet_fourtuple(self, packet, src_ip, src_port, dst_ip, dst_port):
        packet[s.IP].src = src_ip
        packet.sport = src_port
        packet[s.IP].dst = dst_ip
        packet.dport = dst_port

    def _verify_session(self, src_fourtuple):
        if self.sessions.is_src_session_exists(src_fourtuple):
            return
        self.sessions._create_session(src_fourtuple, self.out_iface.ip)

    def add_firewall_rule_chain(self, rule_chain):
        self.firewall.add_rule_chain(rule_chain)


def is_layer_four_packet(packet):
    if packet is None:
        return False
    elif s.IP not in packet or (s.UDP not in packet and s.TCP not in packet):
        return False
    return True