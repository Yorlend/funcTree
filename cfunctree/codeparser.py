import os
from cfunctree.codetree import CodeTree
from pycparser import parse_file
from pycparser.c_parser import CParser
from pycparser.c_ast import NodeVisitor
from tempfile import NamedTemporaryFile
from pcpp import Preprocessor


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


def preprocess(source: str) -> str:
    pre = Preprocessor()
    pre.add_path("./utils/fake_libc_include")
    pre.add_path("/usr/include")
    pre.parse(source)

    tmpfile = NamedTemporaryFile("w", delete=False)
    filename = tmpfile.name

    pre.write(tmpfile)
    tmpfile.close()

    tmpfile = open(filename, "r")
    source = tmpfile.read()
    tmpfile.close()
    os.remove(filename)

    return source


def parse_code(source: str) -> CodeTree:
    source = preprocess(source)

    visitor = CodeVisitor()
    visitor.visit(CParser().parse(source))

    funcs = visitor.get_funcs()
    calls = visitor.get_calls()

    return CodeTree(funcs, calls)
