from Prolog.PrologConsult import *
from Schema.SchemaReader import *
from ReaderXML.ReaderXML import *
from os.path import *
import Commands as Com
import sys
from os.path import *

#pega o caminho da pasta onde o código está sendo executado
path = dirname(realpath(__file__))

#acrescenta os nomes dos arquivos padrões
# isso provavelmente será mudado
path_fact = path + '\\info2.xml'
path_schema = path + '\\schema.xml'

#incializa a leitura do xml e configuação dos grafos
reader = ReaderXML(path_fact)
#incializa as classes que vão adicionar os facts e rules nos arquivos txt
# e faz as chamadas paras instâncias de fact e rule verificarem os vertexs
consult = PrologConsult()
#classe que cria os gerenciadores de cada fact e rule
schema = SchemaReader(path_schema)

#percorro as instâncias de fatos, verifico e adiciono ao arquivo
for fact in schema.facts:
    consult.set_fact(fact, reader.vertexs)

#percorro as instâncias de regras, verifico e adiciono ao arquivo
for rule in schema.rules:
    consult.set_rule(rule)

#fecho a leitura e escrita dos arquivos txt
consult.fact_data.close_file()
consult.rule_data.close_file()

print('Python Ended')


