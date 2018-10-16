import os
from xml.etree import ElementTree


def full_path(xml_name, xml_path):
    file_name = xml_name
    return os.path.abspath(os.path.join(xml_path, file_name))


def load_xml(xml_name, xml_location):
    file_name = xml_name
    full_file_name = os.path.abspath(os.path.join(xml_location, file_name))
    return ElementTree.parse(full_file_name)


def show_all(xml, targets):
    info = xml.findall(targets)
    for i in info:
        print(i)
