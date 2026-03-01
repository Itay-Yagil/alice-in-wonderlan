class Session:
    def __init__(self, original_fourtuple, nat_fourtuple):
        self._original = original_fourtuple
        self._nat = nat_fourtuple

    def get_original(self):
        return self._original

    def get_nat(self):
        return self._nat