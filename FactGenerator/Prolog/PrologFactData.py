from os.path import *
from Functions import *
from Prolog.PrologRule import *


class PrologFactData:
    def __init__(self):
        path = dirname(realpath(__file__))
        file_path = path + '\\facts.txt'
        #print(file_path)
        self.rules = []
        self.file = open(file_path, 'w+')

    def setup_fact(self, name, value1, value2):
        s = name + '(' + value1 + ',' + value2 + ')'
        #print(s)
        self.file.write(s + '\n')
        self.rules.append(PrologRule([name, value1, value2]))

    def close_file(self):
        self.file.close()

    def fact(self, index):
        return self.rules[index]
