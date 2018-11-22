from xml.etree import ElementTree


class SchemaRule:
    def __init__(self, rule):

        self.name = rule.attrib['name']

        rule_inputs = rule.find('inputs')

        inputs = {}

        count = 0
        for inp in rule_inputs:
            for att in inp.attrib:
                inputs[att + '_' + str(count)] = inp.attrib[att]
                count += 1

        self.inputs = inputs

        rule_facts = rule.find('facts')
        facts = {}

        for f in rule_facts:
            facts[f.attrib['name']] = f.find('input').attrib['name']
