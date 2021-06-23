from cfunctree.codetree import CodeTree
from graphviz import Digraph

def graphivy(tree: CodeTree, filename: str):
    dot = Digraph(node_attr={'shape': 'rect'})
    dot.format = 'svg'
    for func in tree.get_func_list():
        dot.node(func, func)
    
    for func in tree.get_func_list():
        for dep in tree.get_dep_list(func):
            dot.edge(func, dep)

    dot.render(filename)
