from xml.etree import ElementTree


class SchemaRule:
    def __init__(self, rules):

        self.rule_name = rules.attrib['name']

        rule_inputs = rules.find('inputs')

        inputs = {}

        count = 0
        for inp in rule_inputs:
            for att in inp.attrib:
                inputs[att + '_' + str(count)] = inp.attrib[att]
                count += 1

        self.inputs = inputs

        rule_facts = rules.find('facts')

        facts = {}

        self.fact_name = rule_facts.attrib['name']

        for f in rule_facts:
            facts[f.attrib['name']] = f.find('input').attrib['name']

        self.facts = facts