from os.path import *
from Functions import *
from Prolog.PrologFact import *


class PrologFactData:
    def __init__(self):
        path = dirname(realpath(__file__))
        file_path = path + '/facts.txt'
        self.facts = []
        self.file = open(file_path, 'w+')

    def setup_fact(self, name, value):
        s = 'fact(' + name + ',' + value + ')'
        print(s)
        self.file.write(s + '\n')
        self.facts.append(PrologFact([name, value]))

    def close_file(self):
        self.file.close()

    def fact(self, index):
        return self.facts[index]
