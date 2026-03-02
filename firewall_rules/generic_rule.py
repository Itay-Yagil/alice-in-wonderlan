from exceptions import StaticClassCreated

class GenericRule:
    def __init__(self):
         raise StaticClassCreated

    @classmethod
    def passes(cls, packet):
        raise NotImplementedError