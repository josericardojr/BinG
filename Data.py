import sys
import threading
import os
import Loader as Loader

from Processor import *
key_quit = 'key_quit'

def run(processor):
    inp = ''
    print('key_test_python')
    while key_quit not in inp:
        inp = input()
        processor.receive_instructions(inp)


char_split = ';'

key_path_prov = 'path_prov'


path_prov = ''

for arg in sys.argv:
    if key_path_prov in str(arg):
        str_split = str(arg).split(char_split)
        if len(str_split) > 1:
            path_prov = str_split[1]


path_config_file = os.path.dirname(os.path.abspath(__file__))
path_config_file = str(path_config_file) + '\config.xml'


path_schema = ''
if os.path.isfile(path_config_file):
    xml = Loader.load_xml(path_config_file)
    path_schema = xml.find('schema_path').text
else:
    print('could not find config.xml at ' + path_config_file)


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