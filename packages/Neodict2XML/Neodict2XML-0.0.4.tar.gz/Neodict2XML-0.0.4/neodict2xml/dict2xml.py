import copy

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='    ')

def from_dict(dict_):
    top_key = list(dict_.keys())[0]
    top = Element(top_key)

    _from_dict_rec(copy.deepcopy(dict_), top_key, top)
    return top

def _from_dict_rec(dict_, top_key, top):
    if isinstance(dict_[top_key], dict):
        for key in dict_[top_key].keys():
            if isinstance(dict_[top_key][key], list):
                tmp_dict = dict_.copy()
                for element in dict_[top_key][key]:
                    ntop = SubElement(top, key)
                    tmp_dict[top_key] = element
                    _from_dict_rec(tmp_dict, top_key, ntop)
            else:
                ntop = SubElement(top, key)
                _from_dict_rec(dict_[top_key], key, ntop)

    elif isinstance(dict_[top_key], tuple):
        for key, value in dict_[top_key][0].items():
            top.set(key, str(value))
        if len(dict_[top_key]) == 2:
            dict_[top_key] = dict_[top_key][1]
            _from_dict_rec(dict_, top_key, top)

    elif dict_[top_key] is not None:
        top.text = str(dict_[top_key])


def from_xml(xml):
    root = ElementTree.fromstring(xml)
    data = {}

    _from_xml_rec(root, data)

    return data

def _from_xml_rec(node, data):
    if len(node) > 0:
        val = {}
        for sub_node in node:
            _from_xml_rec(sub_node, val)
    else:
        val = node.text
        if val is not None:
            val = val.strip()

    key = node.tag
    if len(node.attrib):
        if val is None:
            val = (node.attrib, )
        else:
            val = (node.attrib, val)

    if key in data:
        if isinstance(data[key], list):
            data[key].append(val)
        else:
            data[key] = [data[key], val]
    else:
        data[key] = val
