from XMLReader.Loader import *
from XMLReader.ElementsXML.Vertex import *


class LoadedXML:
    def __init__(self, path):
        xml = loadxml(path)
        vertex = xml.findall('vertices/vertex')
        vertexs = []

        for v in vertex:
            vertexs.append(Vertex(v.find('ID'), v.find('type'), v.find('label'), v.find('date'), v.find('attributes')))

        self.vvertexs = vertexs


    def vertexs(self):
        return self.vvertexs


#aqui eu passei o nome do xml e depois a pasta que ela está
xml = LoadedXML(fullpath('Lucas_2.xml', 'XML'))
#acessando os vertex
vertexs = xml.vertexs()

for v in vertexs:
    # Felipe aqui eu acesso todos os dados por funções
    print('id: {0}\ntype: {1}\nlabel: {2}\ndate: {3}'.format(v.id(), v.type(), v.label(), v.date()))
    # o attributes() retorna uma lista
    atr = v.attributes()
    aux = 0
    for a in atr:
        aux = aux + 1
        print('attributes{0} name: {1} value: {2}'.format(aux, a.name(), a.value()))
    print('_' * 10)




