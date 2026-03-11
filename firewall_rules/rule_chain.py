class RuleChain:
    def __init__(self, *args):
        self.rules = []
        for rule in args:
            self.rules.append(rule)

    def passes(self, packet):
        for rule in self.rules:
            if not rule.relevant(packet):
                return True
        return False