import random
from nat_session import Session
from fourtuple import Fourtuple

SMALLEST_PORT = 10000
HIGHEST_PORT = 65535

class NatSessions:
    def __init__(self):
        self._sessions = []
        self._used_ports = set()

    def is_src_session_exists(self, src_fourtuple):
        for session in self._sessions:
            if session.equals_src(src_fourtuple):
                return True
        return False

    def is_nat_session_exists(self, nat_fourtuple):
        for session in self._sessions:
            if session.equals_nat(nat_fourtuple):
                return True
        return False
    
    def get_src_fourtuple(self, nat_fourtuple):
        for session in self._sessions:
            if session.get_nat() == nat_fourtuple:
                return session.get_src()
        return None
    
    def get_nat_fourtuple(self, src_fourtuple):
        for session in self._sessions:
            if session.get_src() == src_fourtuple:
                return session.get_nat()
        return None

    # Doesn't check if session exists
    def _create_session(self, src_fourtuple: Fourtuple, nat_ip):
        nat_port = random.randrange(SMALLEST_PORT, HIGHEST_PORT + 1)
        while nat_port in self._used_ports:
            nat_port = random.randrange(SMALLEST_PORT, HIGHEST_PORT + 1)
        self._used_ports.add(nat_port)

        self._sessions.append(Session(src_fourtuple.client_ip, src_fourtuple.client_port, nat_ip, nat_port, \
                                      src_fourtuple.server_ip, src_fourtuple.server_port))
        