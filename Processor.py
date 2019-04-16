from kanren import Relation, facts, var, run
from KanrenBing.KanrenBing import *

kanrenBing

# Inicializador, pega a referencia do kanren
class Processor:
    def __init__(self, kanren):
        inputs = \
            {
                'shooter': 'Chaser',
            }

        kanrenBing = kanren
        print(kanrenBing.rules["Teste_valor_input"].run(inputs))


        self.kanrenBing = kanren

def testChaser():
    inputs = \
    {
        'shooter': 'Chaser',
    }
    print(kanrenBing.rules["Teste_valor_input"].run(inputs))

def testArgs(shooter):
    inputs = \
    {
        'shooter': shooter,
    }
    print(kanrenBing.rules["Teste_valor_input"].run(inputs))
    
    
def receive_instructions(self, instructions):
    print(instructions)
