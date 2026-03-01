import random
from nat_session import Session

SMALLEST_PORT = 10000
HIGHEST_PORT = 65535

class NatSessions:
    def __init__(self):
        self._sessions = []
        self._used_ports = set()

    def is_original_session_exists(self, original_fourtuple):
        for session in self._sessions:
            if session.get_original() == original_fourtuple:
                return True
        return False

    def is_nat_session_exists(self, nat_fourtuple):
        for session in self._sessions:
            if session.get_nat() == nat_fourtuple:
                return True
        return False

    def _create_session(self, original_fourtuple, nat_ip):
        nat_port = random.randrange(SMALLEST_PORT, HIGHEST_PORT + 1)
        while nat_port in self._used_ports:
            nat_port = random.randrange(SMALLEST_PORT, HIGHEST_PORT + 1)
        self._used_ports.add(nat_port)

        original_dst_ip = original_fourtuple[2]
        original_dst_port = original_fourtuple[3]
        nat_fourtuple = (nat_ip, nat_port, original_dst_ip, original_dst_port)
        self._sessions.append(Session(original_fourtuple, nat_fourtuple))
        return nat_fourtuple
    
    def get_nat(self, original_fourtuple):
        