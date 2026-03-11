from firewall_rules.generic_rule import GenericRule

class Firewall:
    def __init__(self):
        self.rule_chains = []

    def check(cls, packet):
        for rule_chain in cls.rule_chains:
            if not rule_chain.passes(packet):
                return False
        return True

    def add_rule_chain(cls, rule_chain):
        cls.rule_chains.append(rule_chain)