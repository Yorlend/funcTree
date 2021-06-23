from cfunctree.treegraph import graphivy
from cfunctree.codeparser import parse_code

def test_graphivy():
    for i in range(1, 3):
        c_file = open(f"c_test_files/test_0{i}.c", "r")
        tree = parse_code(c_file.read())
        graphivy(tree, f"tests/out/test_0{i}")
