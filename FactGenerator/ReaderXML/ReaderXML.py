import subprocess
from Functions import *
import Loader as Loader
from XML_Data.Vertex import *


def install(name):
    print('installing ' + name)
    subprocess.call(['pip', 'install', name])


try:
    import networkx as nx
except ImportError:
    install('networkx')
    import networkx as nx


class ReaderXML:
    def __init__(self, path):
        xml = Loader.load_xml(path)
        #inicializa a lib que gera os grafos
        G = nx.Graph()

        #encontra todos os edges, essa função é da lib xml.etree
        edges = xml.findall('edges/edge')

        #aqui para cara edge eu crio as relações para percorrer depois
        for edge in edges:
            #aqui eu só encontro os nomes, que defino nomes padrões
            e_source = source_name(edge.find('sourceID').text)
            e_target = target_name(edge.find('targetID').text)
            #crio a relação
            G.add_edge(e_source, e_target)

            #crio o arquivo para se visualizar o grafo
        nx.write_graphml(G, 'info.graphml ')

        vs = xml.findall('vertices/vertex')
        self.vertexs = {}
        #armazeno os vertexs
        for v in vs:
            self.vertexs[v.find('ID').text] = Vertex(v)
