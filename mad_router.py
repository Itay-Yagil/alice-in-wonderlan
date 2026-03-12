import scapy.all as s
from interface import Interface

class Router:
    def __init__(self, in_iface, out_iface):
        self._in_iface = in_iface
        self._out_iface = out_iface
    
    def run(self):
        while True:
            packet = s.sniff(iface=[self._in_iface.name, self._out_iface.name], count=1)[0]
            packet.show()
            if s.IP not in packet:
                continue
            print(f"Recieved from {packet.sniffed_on}")

            send_to_iface = None
            if packet.sniffed_on == self._in_iface.name:
                send_to_iface = self._out_iface
            else:
                send_to_iface = self._in_iface
            print(f"Sending to {send_to_iface.name}")
            packet.src = send_to_iface.mac
            packet[s.IP].ttl -= 1
            packet.show()
            s.sendp(packet, iface=send_to_iface.name)
            

def main():
    iface1 = Interface("enp0s8", "192.168.64.3", "08:00:27:ad:b5:99")
    iface2 = Interface("enp0s9", "192.168.36.3", "08:00:27:86:a9:6f")
    router = Router(iface1, iface2)
    router.run()

    

if __name__ == "__main__":
    main()