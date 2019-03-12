from os.path import *
from Functions import *
from Prolog.PrologRule import *


class PrologFactData:
    def __init__(self):
        self.facts = []

    def setup_fact(self, name, value1, value2):
        s = name + '(' + value1 + ',' + value2 + ')'
        #print(s)
        self.facts.append(PrologRule([name, value1, value2]))

    def fact(self, index):
        return self.facts[index]
