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
        '''G = nx.Graph()

        edges = xml.findall('edges/edge')

        for edge in edges:
            e_source = source_name(edge.find('sourceID').text)
            e_target = target_name(edge.find('targetID').text)
            G.add_edge(e_source, e_target)

        nx.write_graphml(G, 'info.graphml ')'''

        vs = xml.findall('vertices/vertex')
        self.vertexs = {}

        for v in vs:
            self.vertexs[v.find('ID').text] = Vertex(v)
