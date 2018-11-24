from xml.etree import ElementTree


class Vertex:
    def __init__(self, me):
        self.me = me
        self.ID = me.find('ID').text

    def get_text(self, tag):
        text = 'didn\'t find'

        temp = self.me.find(tag)

        if temp != None:
            text = temp.text
        else:
            text = 'didn\'t find'

        return text
