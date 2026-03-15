import scapy.all as s
from interface import Interface
from routing_table import RoutingTable, Entry

class Router:
    def __init__(self, ifaces, routing_table):
        self._ifaces = ifaces
        self._routing_table = routing_table

    def run(self):
        while True:
            packet = s.sniff(iface=[iface.get_name() for iface in self._ifaces], count=1)[0]
            packet.show()

            if s.IP not in packet:
                continue

            matching_entry = self._routing_table.find_match(packet[s.IP].dst)

            print(f"Recieved from {packet.sniffed_on}")

            if matching_entry != None:
                packet = self._update_packet(packet, matching_entry)
                if packet is not None:
                    print(f"Sending to {matching_entry.get_interface().get_name()}")
                    packet.show()
                    s.sendp(packet, iface=matching_entry.get_interface().get_name())
            else:
                print("No matching entry, dropped")
    
    @staticmethod
    def _update_packet(packet, entry):
        out_iface = entry.get_interface()
        packet.src = out_iface.get_mac()

        dst_mac = None
        if entry.get_gateway() is None:
            dst_mac = s.getmacbyip(packet[s.IP].dst)
        else:
            dst_mac = s.getmacbyip(entry.get_gateway())

        packet.dst = dst_mac
        packet[s.IP].ttl -= 1
        if packet[s.IP].ttl <= 0:
            return None
        
        packet.chksum = None
        return packet


def main():
    iface1 = Interface("enp0s8", "08:00:27:ad:b5:99", "192.168.56.101", "192.168.56.0/24")
    iface2 = Interface("enp0s9", "08:00:27:86:a9:6f", "192.168.5.3", "192.168.5.0/24")
    ifaces = [iface1, iface2]
    entries = [Entry(iface1, iface1.get_subnet(), None),
               Entry(iface2, iface2.get_subnet(), None)]

    routing_table = RoutingTable(entries)
    router = Router(ifaces, routing_table)
    router.run()

if __name__ == "__main__":
    main()