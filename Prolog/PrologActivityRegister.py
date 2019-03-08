from os.path import *
from Functions import *
from Prolog.PrologFact import *


class PrologActivityRegister:
    def __init__(self, key):
        self.activities = []
        self.key = key

    def add_item(self, target):
        self.activities.append(target)
