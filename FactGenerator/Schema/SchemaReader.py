import Loader
import Schema.SchemaFact as schemaFact
import Schema.SchemaRule as schemaRule


key_acess_fact = 'facts/fact'
key_acess_rule = 'rules/rule'

string_input = 'sssP'
#string_input = input()

if 'sssP' in string_input:
    string_input = 'D:\\Documentos\\BinGTool\\FactGenerator\\Schema\\schema.xml'
if 'sssN' in string_input:
    string_input = 'C:\\Users\\nasci\\Documents\\BinGTool\\FactGenerator\\Schema\\schema.xml'


facts = {}

xml = Loader.load_xml(string_input).getroot()

for fact in xml.findall(key_acess_fact):
    schemaFact.SchemaFact(fact)

for rule in xml.findall(key_acess_rule):
    schemaRule.SchemaRule(rule)



