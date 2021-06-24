from cfunctree.treegraph import graphivy
from cfunctree.codeparser import parse_code, parse_files
import sys
import os
from pathlib import Path


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    tree = None

    if len(args) == 1:
        headers = [f for f in Path(".").rglob("*.h")]
        sources = [f for f in Path(".").rglob("*.c")]
        tree = parse_files(headers, sources)

    elif len(args) == 2:
        c_file = open(args[0], "r")
        tree = parse_code(c_file.read())

    if tree is not None:
        graphivy(tree, args[-1])
        os.remove(args[-1])


if __name__ == '__main__':
    sys.exit(main())