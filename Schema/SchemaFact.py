from xml.etree import ElementTree


class SchemaFact:
    def __init__(self, fact):
        attribute_key_splitter = '//'

        self.fact_name = fact.attrib['name']

        info = fact.find('info').attrib

        targets = fact.find('attributes').findall('attrib')
        count = -1
        att_targets = []
        att_filter = []
        self.checkFacts = []

        for t in targets:
            if 'filter' in t.attrib:
                count += 1
                att_filter.append(t.attrib['filter'])
                att_targets.append(t.attrib['target'])

                if attribute_key_splitter in att_targets[count]:
                    splitted = str(att_targets[count]).split(attribute_key_splitter)
                    self.checkFacts.append(lambda vertex: self.get_attribute(vertex, splitted[len(splitted) - 1], att_filter[count]))
                else:
                    self.checkFacts.append(lambda vertex: vertex.me.find(att_targets[count]).text == att_filter[count])
            else:
                att_filter.append('empty')
                self.checkFacts.append(lambda vertex: True)

        if 'value' in info:
            if attribute_key_splitter in info['value']:
                splitted = str(info['value']).split(attribute_key_splitter)
                self.att_value = splitted[len(splitted) - 1]
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

    def check_fact(self, v):
        for check in self.checkFacts:
            if not check(v):
                return False

        return True

    def get_attribute(self, v, key, target_filter):
        for att in v.me.find('attributes'):
            if key in str(att.find('name').text):
                if att.find('value').text == target_filter:
                    return True
                #else:
                    #print(v.me.find('ID').text)
        #print('did not find: ' + key + ' <> ' + self.att_filter[count] + ' index: ' + str(count))
        return False
