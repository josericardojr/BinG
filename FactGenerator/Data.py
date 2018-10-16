import Loader as Loader
from PrologFactGenerator import *
from PrologConsult import *
from os.path import *
import networkx as nx

xml_name = ''
directory_path = ''
while run:
    print('nome do arquivo xml: ')
    xml_name = input()
    print('nome do caminho do arquivo xml: ')
    directory_path = input()

    if isfile(abspath(join(directory_path, xml_name))):
        run = False
        print('carregando')
    else:
        print('o arquivo não existe')

prolog = PrologFactGenerator()
try:
    xml = Loader.load_xml(xml_name, directory_path)

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
    consult = PrologConsult(prolog.facts)
except ValueError:
    print(ValueError)

print('End Python')


