from interface import Interface
from nat import Nat
from firewall_rules.udp_port_rule import UdpPortRule

def main():
    ifaces = []
    ifaces.append(Interface("enp0s8", "192.168.56.101", "08:00:27:ad:b5:99"))
    ifaces.append(Interface("enp0s9", "192.168.56.102", "08:00:27:86:a9:6f"))
    nat = Nat(ifaces[0], ifaces[1])
    nat.add_firewall_rule(UdpPortRule)
    nat.run()


if __name__ == "__main__":
    main()