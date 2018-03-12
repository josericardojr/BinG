from XMLReader.Loader import *
from XMLReader.ElementsXML.Vertex import *


class LoadedXML:
    def __init__(self, path):
        xml = loadxml(path)
        vertex = xml.findall('vertices/vertex')
        vertexs = []

        for v in vertex:
            vertexs.append(Vertex(v.find('ID'), v.find('type'), v.find('label'), v.find('date'), v.find('attributes')))

        for v in vertexs:
            v.myprint()


LoadedXML(fullpath('Lucas_2.xml', 'XML'))


