from cfunctree.codetree import CodeTree
from pycparser.c_parser import CParser
from pycparser.c_ast import FileAST, FuncDecl, FuncCall, FuncDef, NodeVisitor


class CodeVisitor(NodeVisitor):
    def __init__(self):
        self.func_names = set()
        self.func_calls = []
        self.curr_func = ""

    def get_funcs(self):
        return list(self.func_names)

    def get_calls(self):
        return list(set(self.func_calls[:]))

    def visit_FuncDecl(self, node):
        self.func_names.add(node.type.declname)

    def visit_FuncDef(self, node):
        self.func_names.add(node.decl.name)
        self.curr_func = node.decl.name
        self.visit(node.body)

    def visit_FuncCall(self, node):
        self.func_names.add(node.name.name)
        self.func_calls.append((self.curr_func, node.name.name))
        if node.args:
            self.visit(node.args)


def parse_code(source: str) -> CodeTree:
    visitor = CodeVisitor()
    visitor.visit(CParser().parse(source))

    funcs = visitor.get_funcs()
    calls = visitor.get_calls()

    return CodeTree(funcs, calls)
