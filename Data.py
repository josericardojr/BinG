from Prolog.PrologConsult import *
from Schema.SchemaReader import *
from ReaderXML.ReaderXML import *
from os.path import *
import Commands as Com
import sys
from os.path import *


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

consult.fact_data.close_file()
consult.rule_data.close_file()

print('Python Ended')


