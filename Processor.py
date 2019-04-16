from kanren import Relation, facts, var, run
from KanrenBing.KanrenBing import *

class Processor:
    def __init__(self, kanren):
        inputs = \
            {
                'shooter': 'Chaser',
            }

        kanrenBing = kanren
        print(kanrenBing.rules["Teste_valor_input"].run(inputs))


    def receive_instructions(self, instructions):
        print(instructions)
