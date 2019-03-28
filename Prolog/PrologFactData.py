from os.path import *
from Functions import *
from Prolog.PrologFact import *


class PrologFactData:
    def __init__(self):
        self.facts = []

    def setup_fact(self, name, value1, value2):
        self.facts.append(PrologFact([name, value1, value2]))

    def fact(self, index):
        return self.facts[index]
