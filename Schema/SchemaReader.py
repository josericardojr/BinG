import Loader
import Schema.SchemaFact as schemaFact
import Schema.SchemaRule as schemaRule


class SchemaReader:
    def __init__(self, path):
        key_acess_fact = 'facts/fact'
        key_acess_rule = 'rules/rule'

        self.facts = []
        self.rules = []

        xml = Loader.load_xml(path).getroot()

        for fact in xml.findall(key_acess_fact):
            self.facts.append(schemaFact.SchemaFact(fact))
        for rule in xml.findall(key_acess_rule):
            self.rules.append(schemaRule.SchemaRule(rule))
