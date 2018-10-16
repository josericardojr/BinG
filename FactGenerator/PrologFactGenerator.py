from os.path import *
from Functions import *
from PrologFact import *


class PrologFactGenerator:
    def __init__(self):
        path = dirname(realpath(__file__))
        file_path = path + '/facts.txt'
        self.facts = []
        self.file = open(file_path, 'w+')

    def setup_fact(self, first, second, third):
        first = clean_name(first)
        second = clean_name(second)
        third = clean_name(third)
        s = 'fact(' + first + ',' + second + ',' + third + ').'
        #print(s)
        self.file.write(s + '\n')
        self.facts.append(PrologFact([first, second, third]))

    def close_file(self):
        self.file.close()

    def facts(self, index):
        return self.facts[index]