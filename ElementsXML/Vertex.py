class Vertex:
    def __init__(self, vid, vtype, label, date):
        self.id = vid.text
        self.type = vtype.text
        self.label = label.text
        self.date = date.text
        print(self.date)

    def vid(self):
        return self.id

    def vtype(self):
        return self.type

    def label(self):
        return self.label

    def date(self):
        return self.date

    def myprint(self):
        print('id: {0}\ntype: {1}\nlabel: {2}\ndate: {3}'.format(self.vid(), self.vtype(), self.vid(), self.vid()))
        print('_' * 10)
