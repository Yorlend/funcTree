from cfunctree.treegraph import graphivy
from cfunctree.codeparser import parse_code

def test_graphivy_01():
    c_file = open("c_test_files/test_01.cc", "r").read()

    tree = parse_code(c_file)

    graphivy(tree, "test")

def test_graphivy_02():
    c_file = open("c_test_files/test_02.cc", "r").read()

    tree = parse_code(c_file)

    graphivy(tree, "test")