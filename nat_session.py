from fourtuple import Fourtuple

class Session:
    def __init__(self, src_ip, src_port, nat_ip, nat_port, dst_ip, dst_port):
        self.src_ip = src_ip
        self.src_port = src_port
        self.nat_ip = nat_ip
        self.nat_port = nat_port
        self.dst_ip = dst_ip
        self.dst_port = dst_port

    def get_src(self):
        return Fourtuple(self.src_ip, self.src_port, self.dst_ip, self.dst_port)

    def get_nat(self):
        return Fourtuple(self.nat_ip, self.nat_port, self.dst_ip, self.dst_port)
    
    def equals_src(self, src_fourtuple):
        if src_fourtuple == self.get_src():
            return True
        return False
    
    def equals_nat(self, nat_fourtuple):
        if nat_fourtuple == self.get_nat():
            return True
        return False
    
    def __str__(self):
        return f"{self.src_ip}:{self.src_port} - {self.nat_ip}:{self.nat_port} - {self.dst_ip}:{self.dst_port}"