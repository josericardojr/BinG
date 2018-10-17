from kanren import *
import Commands as Com
import sys


class PrologConsult:
    def __init__(self, ready_facts):
        self.facts = ready_facts

        relation = Relation()

        for fact in self.facts:
            facts(relation, fact.get_facts())

        x = var()
        y = var()
        z = var()
        result = run(sys.maxsize, x, (relation, y, z, x))
        print(Com.command_feedback(result))
