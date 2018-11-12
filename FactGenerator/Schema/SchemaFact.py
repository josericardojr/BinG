from xml.etree import ElementTree


class SchemaFact:
    def __init__(self, fact):

        self.name = fact.attrib['name']

        att = fact.find('attrib').attrib

        self.att_name = att['name']
        self.att_filter = att['filter']
        self.att_value = att['value']

        '''msg = 'fact: ' + self.name + '\n'
        msg += 'name: ' + self.att_name + '\n'
        msg += 'filter: ' + self.att_filter + '\n'
        msg += 'value: ' + self.att_value + '\n'
        msg += '_' * 10
        print(msg)'''
