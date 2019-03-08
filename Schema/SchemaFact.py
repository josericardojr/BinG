from xml.etree import ElementTree


class SchemaFact:
    def __init__(self, fact):

        attribute_key_spliter = '//'
        self.name = fact.attrib['name']

        info = fact.find('info').attrib

        targets = fact.find('attributes').findall('attrib')
        count = -1
        self.att_targets = []
        self.att_filter = []
        self.checkFacts = []


        for t in targets:
            if 'filter' in t.attrib:
                count += 1
                self.att_filter.append(t.attrib['filter'])
                self.att_targets.append(t.attrib['target'])
                if attribute_key_spliter in self.att_targets[count]:
                    splited = str(self.att_targets[count]).split(attribute_key_spliter)
                    self.checkFacts.append(lambda vertex: self.get_attribute(vertex, splited[len(splited) - 1], count))
                else:
                    self.checkFacts.append(lambda vertex: vertex.me.find(self.att_targets[count]).text == self.att_filter[count])
            else:
                self.att_filter.append('empty')
                self.checkFacts.append(lambda vertex: True)

        if 'value' in info:
            if attribute_key_spliter in info['value']:
                splited = str(info['value']).split(attribute_key_spliter)
                self.att_value = splited[len(splited) - 1]
                self.get_value = lambda vertex: self.get_text_attribute(vertex, self.att_value)

            else:
                self.att_value = info['value']
                self.get_value = lambda vertex: self.get_text_standard(vertex, self.att_value)
        else:
            self.att_value = 'without value'
            self.get_value = lambda vertex: False

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

    def checkFact(self, v):
        count = -1
        for target in self.att_targets:
            count += 1
            if not self.checkFacts[count](v):
                return False

        return True

    def get_attribute(self, v, key, count):
        count-=1
        for att in v.me.find('attributes'):
            if key in str(att.find('name').text):
                if att.find('value').text == self.att_filter[count]:
                    return True
                #else:
                    #print(v.me.find('ID').text)
        #print('did not find: ' + key + ' <> ' + self.att_filter[count] + ' index: ' + str(count))
        return False
