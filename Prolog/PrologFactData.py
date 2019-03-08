from os.path import *
from Functions import *
from Prolog.PrologRule import *


class PrologFactData:
    def __init__(self):
        self.rules = []

    def setup_fact(self, name, value1, value2):
        s = name + '(' + value1 + ',' + value2 + ')'
        print(s)
        self.rules.append(PrologRule([name, value1, value2]))

    def fact(self, index):
        return self.rules[index]
