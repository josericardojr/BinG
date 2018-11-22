from Prolog.PrologConsult import *
from Schema.SchemaReader import *
from os.path import *
import Commands as Com

string_input = ''
path_fact = ''
path_schema = ''
run = True
last_command = Com.command_ask_path()
while run:
    print(last_command)
    string_input = input()
    if 'sssP' in string_input:
        path_fact = 'D:\\Documentos\\BinGTool\\FactGenerator\\info2.xml'
        path_schema = 'D:\\Documentos\\BinGTool\\FactGenerator\\Schema\\schema.xml'
    if 'sssN' in string_input:
        path_fact = 'C:\\Users\\nasci\\Documents\\BinGTool\\FactGenerator\\info2.xml'
        path_schema = 'C:\\Users\\nasci\\Documents\\BinGTool\\FactGenerator\\Schema\\schema.xml'
    if string_input in Com.command_quit():
        run = False
    elif isfile(path_fact):
        run = False
        print(Com.command_feedback('loading'))
    else:
        print(Com.command_feedback('err ' + path_fact))


consult = PrologConsult(path_fact)
schema = SchemaReader(path_schema)


print('Python Ended')


