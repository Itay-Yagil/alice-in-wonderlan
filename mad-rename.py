import scapy.all as s
from interface import Interface

class Router:
    def __init__(self, ifaces):
        self.sockets = []
        for iface in ifaces:
            sock = s.conf.L2socket(iface=iface.name)
            self.sockets.append(sock)
    
    def run(self):
        while True:
            packet = self.sockets[0].recv()
            if type(packet) != None:
                self.sockets[1].send(packet)

def main():
    ifaces = []
    ifaces.append(Interface("enp0s3"))
    ifaces.append(Interface("enp0s8"))
    router = Router(ifaces)
    router.run()

    

if __name__ == "__main__":
    main()