import Loader as Loader
import Commands as Com
from PrologFactGenerator import *
from PrologConsult import *
from os.path import *
import networkx as nx

string_input = ''
run = True
last_command = Com.command_ask_path()
while run:
    print(last_command)
    string_input = input()

    if string_input == Com.command_quit():
        run = False
    elif isfile(string_input):
        run = False
    else:
        print(Com.command_feedback('err ' + string_input))

if string_input != Com.command_quit():
    print(Com.command_feedback('loading'))
    try:
        prolog = PrologFactGenerator()
        xml = Loader.load_xml(string_input)

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
    except ValueError:
        print(ValueError)

run = True

consult = PrologConsult(prolog.facts)
while run:
    if string_input == Com.command_quit():
        run = False
    print('waiting the end ' + Com.command_quit())
    string_input = input()

print('Python Ended')


