import os
from cfunctree import utils
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
        try:
            self.func_names.add(node.type.declname)
        except:
            pass

    def visit_FuncDef(self, node):
        self.func_names.add(node.decl.name)
        self.curr_func = node.decl.name
        self.visit(node.body)

    def visit_FuncCall(self, node):
        if type(node.name.name) is str:
            self.func_names.add(node.name.name)
            self.func_calls.append((self.curr_func, node.name.name))
        if node.args:
            self.visit(node.args)


def build_preprocessor() -> Preprocessor:
    pre = Preprocessor()
    pre.add_path(os.path.abspath(utils.__file__)[:-11] + "fake_libc_include")
    pre.add_path("/usr/include")
    pre.add_path("/usr/local/include")
    return pre


def preprocess(source: str, pre: Preprocessor) -> str:
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
    pre = build_preprocessor()
    source = preprocess(source, pre)

    visitor = CodeVisitor()
    visitor.visit(CParser().parse(source))

    funcs = visitor.get_funcs()
    calls = visitor.get_calls()

    return CodeTree(funcs, calls)


def parse_files(headers: list, sources: list) -> CodeTree:
    funcs = set()
    calls = set()
    for sourcefile in sources:
        pre = build_preprocessor()
        for header in headers:
            pre.add_path(header.parent)
        src = open(sourcefile, "r").read()
        src = preprocess(src, pre)
        try:
            tree = parse_code(src)
            funcs.update(tree.funcs)
            calls.update(tree.calls)
        except Exception as e:
            print("could not parse file:", sourcefile)
            print("error at", str(e))

    return CodeTree(list(funcs), list(calls))
