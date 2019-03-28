from os.path import *
from Functions import *
from Prolog.PrologRule import *
from Prolog.PrologRule import PrologRule


class PrologRuleData:
    def __init__(self):
        self.rules = []

    def setup_rule(self, rule):
        self.rules.append(rule)

    def get_rule(self, index):
        return self.rules[index]
