from xml.etree import ElementTree


class SchemaRule:
    def __init__(self, rules):

        self.rule_name = rules.attrib['name']

        rule_inputs = rules.find('inputs')
        r = rules.find('return')
        self.return_var = r.attrib['name']

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
            facts[f.attrib['name']] = []
            for inp in f:
                facts[f.attrib['name']].append(inp.attrib['name'])

        find = False
        for f1 in facts:
            for f2 in facts[f1]:
                if self.return_var == f2:
                    find = True

        if not find:
            SchemaRule.error_feedback(self.rule_name + ' do not have any fact\'s input named: ' + self.return_var)

        self.facts = facts

    def get_return_var(self):
        return self.return_var

    @staticmethod
    def error_feedback(s):
        print("ERROR:")
        print(s)
        print('<>' * 3)
