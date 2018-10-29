from Prolog.PrologConsult import *
from os.path import *
import Commands as Com

string_input = ''
run = True
last_command = Com.command_ask_path()
while run:
    print(last_command)
    string_input = input()
    if 'sssP' in string_input:
        string_input = 'D:\Documentos\BinGTool\FactGenerator\info2.xml'
    if 'sssN' in string_input:
        string_input = 'C:\\Users\\nasci\\Documents\\BinGTool\\FactGenerator\\info2.xml'
    if string_input in Com.command_quit():
        run = False
    elif isfile(string_input):
        run = False
        print(Com.command_feedback('loading'))
    else:
        print(Com.command_feedback('err ' + string_input))


consult = PrologConsult(string_input)
run = True
while run:
    if string_input in Com.command_quit():
        run = False
    else:
        consult.execute_command(string_input)
        string_input = input()


print('Python Ended')


