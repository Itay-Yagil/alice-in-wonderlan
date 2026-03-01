import scapy.all as s
import select
from interface import Interface

class Proxy:
    def __init__(self, in_iface, out_iface):
        self.proxy_address = None
        self.in_iface = in_iface
        self.out_iface = out_iface
        self.in_sock = s.conf.L2socket(self.in_iface.name)
        self.out_sock = s.conf.L2socket(self.out_iface.name)
    
    def run(self):
        while True:
            readable, _, _ = select.select([self.in_sock, self.out_sock], [], [])

            for sock in readable:
                if sock is self.in_sock:
                    self._to_out_proxy()
                elif sock is self.out_sock:
                    self._to_in_proxy()

    def _to_out_proxy(self):
        packet = self.in_sock.recv()
        if s.IP not in packet:
            print("Not a layer 3 packet...")
            return
        self.proxy_address = (packet[s.Ether].src, packet[s.IP].src)
        packet[s.Ether].src = self.out_iface.mac
        packet[s.IP].src = self.out_iface.ip
        self.out_sock.send(packet)

    def _to_in_proxy(self):
        packet = self.in_sock.recv()
        if self.proxy_address is None:
            print("No proxy exists...")
            return
        elif s.IP not in packet:
            print("Not a layer 3 packet...")
            return
        packet[s.Ether].dst = self.proxy_address[0]
        packet[s.IP].dst = self.proxy_address[1]
        self.in_sock.send(packet)

def main():
    ifaces = []
    ifaces.append(Interface("enp0s8", "192.168.56.101", "08:00:27:1b:96:26"))
    ifaces.append(Interface("enp0s9", "192.168.56.102", "08:00:27:b0:5a:7a"))
    proxy = Proxy(ifaces[0], ifaces[1])
    proxy.run()

    

if __name__ == "__main__":
    main()