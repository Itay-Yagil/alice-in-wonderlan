import scapy.all as s
from interface import Interface
from routing_table import RoutingTable, Entry

class Router:
    def __init__(self, ifaces, routing_table):
        self.sockets = []
        self._ifaces = ifaces
        self._routing_table = routing_table
    
    def run(self):
        while True:
            packet = s.sniff(iface=[iface.name for iface in self._ifaces], count=1)[0]
            out_iface = self._routing_table.find_match(packet[s.IP].dst)
            if out_iface != None:
                packet.src = out_iface.mac
                packet[s.IP].ttl -= 1
                s.sendp(packet, iface=out_iface.name)
            

def main():
    iface1 = Interface("enp0s8", "192.168.56.101", "08:00:27:ad:b5:99")
    iface2 = Interface("enp0s9", "192.168.56.102", "08:00:27:86:a9:6f")
    ifaces = [iface1, iface2]
    routing_table = RoutingTable([Entry(iface1, "192.168.56.101/32"), Entry(iface2, "0.0.0.0/0")])
    router = Router(ifaces, routing_table)
    router.run()

    

if __name__ == "__main__":
    main()