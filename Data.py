import sys
import threading
import time
from os.path import *
from Prolog.PrologConsult import *
from Schema.SchemaReader import *
from ReaderXML.ReaderXML import *
from Processor import *
import Commands as Com
from KanrenBing.KanrenBing import *
key_quit = 'key_quit'

def run(processor):
    inp = ''
    print('key_test_python')
    while key_quit not in inp:
        inp = input()
        processor.receive_instructions(inp)


char_split = ';'

key_path_prov = 'path_prov'
key_path_schema = 'path_schema'


path_prov = ''
path_schema = ''

for arg in sys.argv:
    if key_path_prov in str(arg):
        str_split = str(arg).split(char_split)
        if len(str_split) > 1:
            path_prov = str_split[1]

    if key_path_schema in str(arg):
        str_split = str(arg).split(char_split)
        if len(str_split) > 1:
            path_schema = str_split[1]




processor = Processor(path_prov, path_schema)
print('KEY_PATH_READY')
t = threading.Thread(target=run, args=(processor,))
t.start()
'''
inputs =\
    {
      'shooter': 'Chaser',
    }

for r_name in kanren.rules:
    print('<>' * 3)
    print('Using rule: ' + r_name)
    KanrenBing.normalize_result(kanren.rules[r_name].run(inputs))'''