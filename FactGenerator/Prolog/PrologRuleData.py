from os.path import *
from Functions import *
from Prolog.PrologRule import *
from Prolog.PrologRule import PrologRule


class PrologRuleData:
    def __init__(self):
        path = dirname(realpath(__file__))
        file_path = path + '\\rules.txt'
        #print(file_path)
        self.rules = []
        self.file = open(file_path, 'w+')

    def setup_rule(self, rule):
        s = rule.rule_name + '('
        #print(s)

        count = len(rule.inputs)
        i = 0
        for inp in rule.inputs:
            s += rule.inputs[inp]
            i += 1
            if i < count:
                s += ','

        s += '):-' + rule.fact_name + '('

        count = len(rule.facts)
        i = 0
        for fact in rule.facts:
            s += rule.facts[fact]
            i += 1
            if i < count:
                s += ','

        s += ').'
        #print(s)
        self.file.write(s + '\n')
        self.rules.append(PrologRule(s))

    def close_file(self):
        self.file.close()

    def get_rule(self, index):
        return self.rules[index]
