from Prolog.PrologConsult import *
from Schema.SchemaReader import *
from ReaderXML.ReaderXML import *
from Processor import *
from os.path import *
import Commands as Com
import sys
from os.path import *
from KanrenBing.KanrenBing import *

path = dirname(realpath(__file__))

path_fact = path + '\\info2.xml'
path_schema = path + '\\schema.xml'

reader = ReaderXML(path_fact)
consult = PrologConsult()
schema = SchemaReader(path_schema)

for fact in schema.facts:
    consult.set_fact(fact, reader.vertexs)

for rule in schema.rules:
    consult.set_rule(rule)


kanren = KanrenBing(consult)

processor = Processor(kanren)

inputs =\
    {
      'shooter': 'Round_-20444',
    }

for r_name in kanren.rules:
    print('<>' * 3)
    print('Using rule: ' + r_name)
    KanrenBing.normalize_result(kanren.rules[r_name].run(inputs))
