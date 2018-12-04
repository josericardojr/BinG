from xml.etree import ElementTree


class Vertex:
    def __init__(self, me):
        self.me = me
        self.ID = me.find('ID').text
