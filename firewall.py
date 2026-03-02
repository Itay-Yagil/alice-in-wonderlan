from firewall_rules.generic_rule import GenericRule

class Firewall:
    def __init__(self):
        self.rules = []

    def check(cls, packet):
        for rule in cls.rules:
            if not rule.passes(packet):
                return False
        return True

    def add_rule(cls, rule):
        cls.rules.append(rule)
