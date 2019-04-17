from Prolog.PrologConsult import *
from Schema.SchemaReader import *
from ReaderXML.ReaderXML import *
from kanren import Relation, facts, var, run
from KanrenBing.KanrenBing import *


tratamentoDeDadosTeste =	{
  "Tag1": "Dado1",
  "Tag2": "Dado2",
}

# Inicializador, pega a referencia do kanren
class Processor:
    def __init__(self, path_prov, path_schema):
        self.setup_bing(path_prov, path_schema)
        inputs = \
            {
                'shooter': 'Chaser',
            }

        print(self.kanrenBing.rules["Teste_valor_input"].run(inputs))

    def setup_bing(self, path_prov, path_schema):
        print(path_prov)
        self.path_schema = path_schema
        reader = ReaderXML(path_prov)
        consult = PrologConsult()
        schema = SchemaReader(path_schema)

        for f in schema.facts:
            consult.set_fact(f, reader.vertexs)

        for rule in schema.rules:
            consult.set_rule(rule)

        kanren = KanrenBing(consult)
        self.kanrenBing = kanren

    def testChaser(self, ):
        inputs = \
        {
            'shooter': 'Chaser',
        }
        print(self.kanrenBing.rules["Teste_valor_input"].run(inputs))

    def testArgs(self, shooter):
        inputs = \
        {
            'shooter': shooter,
        }
        print(self.kanrenBing.rules["Teste_valor_input"].run(inputs))


    def receive_instructions(self, instructions):
        print(instructions)
        tratamentoDeDadosTeste["Tag1"] = "new Instruction"
        tratamentoDeDadosTeste["Tag2"] = "new Instruction2"

    def send_instructions(self):
        print("") # Envia via Print o resultado final do processamento
