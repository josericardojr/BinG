from os.path import *
from Functions import *
from PrologFact import *


class PrologActivityRegister:
    def __init__(self, key):
        self.activities = []
        self.key = key

    def add_item(self, target):
        print(self.key + ': ' + target)
        self.activities.append(target)
