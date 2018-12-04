from xml.etree import ElementTree


class SchemaFact:
    def __init__(self, fact):

        self.name = fact.attrib['name']

        att = fact.find('attrib').attrib

        self.att_target = att['target']

        attribute_key_spliter = '//'

        if 'filter' in att:
            self.att_filter = att['filter']
            if attribute_key_spliter in self.att_target:
                splited = str(self.att_target).split(attribute_key_spliter)
                self.checkFact = lambda vertex: self.get_attribute(vertex, splited[len(splited) - 1])
            else:
                self.checkFact = lambda vertex: vertex.me.find(self.att_target).text == self.att_filter
        else:
            self.att_filter = ''
            self.checkFact = lambda vertex: True

        if 'value' in att:
            if attribute_key_spliter in att['value']:
                splited = str(att['value']).split(attribute_key_spliter)
                self.att_value = splited[len(splited) - 1]
                self.get_value = lambda vertex: self.get_text_attribute(vertex, self.att_value)

            else:
                self.att_value = att['value']
                self.get_value = lambda vertex: self.get_text_standard(vertex, self.att_value)
        else:
            self.att_value = self.att_target
            self.get_value = lambda vertex: self.get_text_standard(vertex, self.att_value)

    def get_text_standard(self, vertex, tag):
        text = 'didn\'t find'

        temp = vertex.me.find(tag)

        if temp != None:
            text = temp.text
        else:
            text = 'didn\'t find'

        return text

    def get_text_attribute(self, vertex, tag):
        text = 'didn\'t find'
        temp = ''
        for att in vertex.me.find('attributes'):
            if tag in str(att.find('name').text):
                temp = att.find('value').text

        if temp != None:
            text = temp
        else:
            text = 'didn\'t find'


        return text

    def get_attribute(self, v, key):
        for att in v.me.find('attributes'):
            if key in str(att.find('name').text):
                if att.find('value').text == self.att_filter:
                    return True
        return False
