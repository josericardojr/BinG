from kanren import Relation, facts, var, run
from KanrenBing.KanrenBing import *

kanrenBing

tratamentoDeDadosTeste =	{
  "Tag1": "Dado1",
  "Tag2": "Dado2",
}

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
    tratamentoDeDadosTeste["Tag1"] = "new Instruction"
    tratamentoDeDadosTeste["Tag2"] = "new Instruction2"

def send_instructions(self):
    print("") # Envia via Print o resultado final do processamento
