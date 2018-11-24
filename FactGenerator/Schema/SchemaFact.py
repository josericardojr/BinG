from xml.etree import ElementTree


class SchemaFact:
    def __init__(self, fact):

        self.name = fact.attrib['name']

        att = fact.find('attrib').attrib

        self.att_name = att['name']

        if 'filter' in att:
            self.att_filter = att['filter']
            self.checkFact = lambda vertex: vertex.me.find(self.att_name).text == self.att_filter
        else:
            self.att_filter = ''
            self.checkFact = lambda vertex: True

        if 'value' in att:
            self.att_value = att['value']
        else:
            self.att_value = ''
