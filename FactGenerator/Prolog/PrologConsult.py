import subprocess
import sys
import Loader as Loader
import Commands as Com
from XML_Data.Vertex import *
from Prolog.PrologFactGenerator import *
from Prolog.PrologActivityRegister import *


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
        prolog = PrologFactGenerator()
        xml = Loader.load_xml(path)

        G = nx.Graph()

        edges = xml.findall('edges/edge')

        for edge in edges:
            e_source = source_name(edge.find('sourceID').text)
            e_target = target_name(edge.find('targetID').text)
            G.add_edge(e_source, e_target)

        activity_founded = {}
        vs = xml.findall('vertices/vertex')

        vertexs = {}
        for vertex in vs:
            if vertexs[vertex].me.find('type').text in 'Activity':
                activity_name = vertexs[vertex].me.find('label').text

                if activity_name not in activity_founded:
                    activity_founded[activity_name] = PrologActivityRegister(activity_name)

                name_vertex = source_name(vertexs[vertex].me.find('ID').text)
                if name_vertex in G.nodes:
                    for target in G[name_vertex]:
                        if vertexs[clean_name(target)].me.find('type').text not in 'Activity':
                            activity_founded[activity_name].add_item(clean_name(target))
                            print(activity_name + '<>'+ vertexs[vertex].me.find('ID').text + ': ' + clean_name(target))
            vertexs[vertex.find('ID').text] = Vertex(vertex)
        '''for vertex in vertexs:
            name_target = target_name(vertexs[vertex].me.find('ID').text)
            if name_target in G.nodes:
                first_vertex = target_to_source_name(name_target)
                for second_vertex in G[name_target]:
                    name_target = source_to_target_name(second_vertex)
                    if name_target in G.nodes:
                        for third_vertex in G[name_target]:
                            prolog.setup_fact(first_vertex, second_vertex, third_vertex)

        '''

        self.facts = prolog.facts

        print(Com.command_feedback('ready'))

    def execute_command(self, command):
        if command in Com.command_repeat():
            self.consult()

    def consult(self):
        relation = Relation()

        for f in self.facts:
            facts(relation, f.get_facts())

        x = var()
        y = var()
        z = var()
        result = run(sys.maxsize, x, (relation, y, z, x))
        print(Com.command_feedback(''.join(result)))
