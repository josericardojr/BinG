from os.path import *
from Functions import *
from Prolog.PrologRule import *
from Prolog.PrologRule import PrologRule


class PrologRuleData:
    def __init__(self):
        self.rules = []

    def setup_rule(self, rule):
        s = rule.rule_name + '('
        #print(s)

        length = len(rule.inputs)
        i = 0
        for inp in rule.inputs:
            s += rule.inputs[inp]
            i += 1
            if i < length:
                s += ','

        s += '):-\n\t'

        count = len(rule.facts)
        for fact in rule.facts:
            length = len(rule.facts[fact])
            s += fact + '('

            for inp in rule.facts[fact]:
                s += inp
                length -= 1

                if length > 0:
                    s += ','

            count -= 1
            if count > 0:
                s += '),\n\t'

        s += ').'
        print(s)
        self.rules.append(PrologRule(s))

    def get_rule(self, index):
        return self.rules[index]
