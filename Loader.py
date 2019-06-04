import os
from xml.etree import ElementTree


def full_path(xml_name, xml_path):
    file_name = xml_name
    return os.path.abspath(os.path.join(xml_path, file_name))


def load_xml(path):
    return ElementTree.parse(path)


def show_all(xml, targets):
    info = xml.findall(targets)
    for i in info:
        print(i)
