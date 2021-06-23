from cfunctree.treegraph import graphivy
from cfunctree.codeparser import parse_code
import sys
import os

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    c_file = open(args[0], "r")
    tree = parse_code(c_file.read())
    graphivy(tree, args[1])
    os.remove(args[1])


if __name__ == '__main__':
    sys.exit(main())