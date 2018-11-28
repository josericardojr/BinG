from Prolog.PrologConsult import *
from Schema.SchemaReader import *
from os.path import *
import Commands as Com
import sys

string_input = ''
path_fact = ''
path_schema = ''
run = True
last_command = Com.command_ask_path()

for arg in sys.argv:
    string_input = arg
    if 'sssP' in string_input:
        path_fact = 'D:\\Documentos\\BinGTool\\FactGenerator\\info2.xml'
        path_schema = 'D:\\Documentos\\BinGTool\\FactGenerator\\Schema\\schema.xml'
    if 'sssN' in string_input:
        path_fact = 'C:\\Users\\nasci\\Documents\\BinGTool\\FactGenerator\\info2.xml'
        path_schema = 'C:\\Users\\nasci\\Documents\\BinGTool\\FactGenerator\\Schema\\schema.xml'

consult = PrologConsult(path_fact)
schema = SchemaReader(path_schema)

for fact in schema.facts:
    consult.set_fact(fact)

for rule in schema.rules:
    consult.set_rule(rule)

consult.fact_data.close_file()

print('Python Ended')


