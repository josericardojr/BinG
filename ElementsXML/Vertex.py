from XMLReader.ElementsXML.Attributes import *


class Vertex:
    def __init__(self, vid, vtype, label, date, attributes):
        self.id = vid.text
        self.type = vtype.text
        self.label = label.text
        self.date = date.text
        atr = []
        for a in attributes:
            atr.append(Attributes(a.find('name').text, a.find('value').text))
        self.attributes = atr

    def vid(self):
        return self.id

    def vtype(self):
        return self.type

    def label(self):
        return self.label

    def date(self):
        return self.date

    def attributes(self):
        return self.attributes

    def myprint(self):
        print('id: {0}\ntype: {1}\nlabel: {2}\ndate: {3}'.format(self.vid, self.vtype, self.label, self.date))
        atr = self.attributes
        print('=' * 10)
        #for a in atr:
            #print('{0}: {1}'.format(a.name(), a.value()))
        print('_' * 10)
