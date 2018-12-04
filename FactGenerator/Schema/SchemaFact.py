from xml.etree import ElementTree


class SchemaFact:
    def __init__(self, fact):

        self.name = fact.attrib['name']

        att = fact.find('attrib').attrib

        self.att_name = att['target']

        attribute_key_spliter = '//'

        if 'filter' in att:
            self.att_filter = att['filter']
            if attribute_key_spliter in self.att_name:
                splited = str(self.att_name).split(attribute_key_spliter)
                self.checkFact = lambda vertex: self.tst(vertex, splited[len(splited) - 1])
            else:
                self.checkFact = lambda vertex: vertex.me.find(self.att_name).text == self.att_filter
        else:
            self.att_filter = ''
            self.checkFact = lambda vertex: True

        if 'value' in att:
            self.att_value = att['value']
        else:
            self.att_value = self.att_name

    def tst(self, v, key):
        for att in v.me.find('attributes'):
            if key in str(att.find('name').text):
                if att.find('value').text == self.att_filter:
                    return True
        return False
