from Prolog.PrologFactData import *
from Prolog.PrologRuleData import *


class PrologConsult:
    def __init__(self):
        self.fact_data = PrologFactData()
        self.rule_data = PrologRuleData()

    def set_fact(self, f, vertexs):
        for v in vertexs:
            if f.check_fact(vertexs[v]):
                self.fact_data.setup_fact(f.fact_name, vertexs[v].ID, f.get_value(vertexs[v]))

    def set_rule(self, r):
        self.rule_data.setup_rule(r)
