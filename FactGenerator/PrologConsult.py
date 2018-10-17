from kanren import *
import sys
import Loader as Loader
import networkx as nx
import Commands as Com
from PrologFactGenerator import *


class PrologConsult:
    def __init__(self, path):
        prolog = PrologFactGenerator()
        xml = Loader.load_xml(path)

        G = nx.Graph()

        edges = xml.findall('edges/edge')

        for edge in edges:
            eSource = source_name(edge.find('sourceID').text)
            eTarget = target_name(edge.find('targetID').text)
            G.add_edge(eSource, eTarget)

        vertexs = xml.findall('vertices/vertex')
        for vertex in vertexs:
            nameTarget = target_name(vertex.find('ID').text)
            if nameTarget in G.nodes:
                first_vertex = target_to_source_name(nameTarget)
                for second_vertex in G[nameTarget]:
                    nameTarget = source_to_target_name(second_vertex)
                    if nameTarget in G.nodes:
                        for third_vertex in G[nameTarget]:
                            prolog.setup_fact(first_vertex, second_vertex, third_vertex)

        prolog.close_file()

        self.facts = prolog.facts

        print(Com.command_feedback('ready'))

    def execute_command(self, command):
        if command in Com.command_repeat():
            self.consult()

    def consult(self):
        relation = Relation()

        for fact in self.facts:
            facts(relation, fact.get_facts())

        x = var()
        y = var()
        z = var()
        result = run(sys.maxsize, x, (relation, y, z, x))
        print(Com.command_feedback(''.join(result)))
