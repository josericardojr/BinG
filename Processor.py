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

        '''Instancio o dicionário'''
        self.methods = {}
        key = 'key_test_python'
        '''adiciono um método com a função que criei'''
        '''passo a chave do método e o método'''
        self.add_method(key, self.example_method)

        key = 'player_damage'
        self.add_method(key, self.fire_damage)

        key = '2Enemy'
        self.add_method(key, self.chaserandstraight)

    def chaserandstraight(self):
        inputs = \
            {
                'shooter': 'Straight',
            }
        inputs2 = \
            {
                'shooter': 'Chaser',
            }
        if len(self.kanrenBing.rules["PlayerHit"].run(inputs)) > 0 & \
                len(self.kanrenBing.rules["PlayerHit"].run(inputs2)):
            print("chaser&straight;true")
        else:
            print("chaser&straight;false")


    def fire_damage(self):
        inputs = \
            {
                'shooter': 'Chaser',
            }
        print('_' * 5)
        print('hi i am a player_damage example')
        print('calling rule: \'Teste_valor_input\'')
        print(self.kanrenBing.rules["PlayerHit"].run(inputs))

    def example_method(self):
        inputs = \
            {
                'shooter': 'Chaser',
            }

        print('_' * 5)
        print('hi i am an example')
        print('calling rule: \'Teste_valor_input\'')
        print(self.kanrenBing.rules["PlayerHit"].run(inputs))

    def add_method(self, method_key, method):
        if method_key not in self.methods:
            self.methods[method_key] = method
        else:
            print('error: method_key already exists')


    def setup_bing(self, path_prov, path_schema):
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
        i  = 'key;funPlayerDamage'
        tratamentoDeDadosTeste["funPlayerDamage"] = "new Instruction"
        tratamentoDeDadosTeste["Tag2"] = "new Instruction2"

        '''verifico se tem um método com o nome, caso tenha eu chamo'''
        if instructions in self.methods:
            self.methods[instructions]()

    def send_instructions(self, key , msg):
        print("") # Envia via Print o resultado final do processamento
