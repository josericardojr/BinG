import subprocess
import Loader as Loader
from XML_Data.Vertex import *
from Functions import *
from  Prolog.PrologFactData import *
from Schema.SchemaFact import *

def install(name):
    print('installing ' + name)
    subprocess.call(['pip', 'install', name])


try:
    from kanren import *
except ImportError:
    install('kanren')
    from kanren import *

try:
    import networkx as nx
except ImportError:
    install('networkx')
    import networkx as nx


class PrologConsult:
    def __init__(self, path):
        xml = Loader.load_xml(path)
        self.fact_data = PrologFactData()
        G = nx.Graph()

        edges = xml.findall('edges/edge')

        for edge in edges:
            e_source = source_name(edge.find('sourceID').text)
            e_target = target_name(edge.find('targetID').text)
            G.add_edge(e_source, e_target)

        nx.write_graphml(G, 'info.graphml ')

        vs = xml.findall('vertices/vertex')
        self.vertexs = {}

        for v in vs:
            self.vertexs[v.find('ID').text] = Vertex(v)

    def set_fact(self, fact):
        for v in self.vertexs:
            if self.vertexs[v].me.find(fact.att_name).text in fact.att_filter:
                self.fact_data.setup_fact(fact.name, self.vertexs[v].me.find(fact.att_name).text)
