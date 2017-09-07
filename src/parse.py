from src.expr_tree import ExprTree 
from src.bfs import bfs

FILE = "input/theorem.out"

def parse_lines(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        lines = lines.splitlines()
    return lines 

def extract_lines(lines):
    data_list = []
    for line in lines:

        expr = line.strip() 
        if expr.startswith('atom '):
            expr = expr[len('atom '):]
            depth = line.count(' ')
            data_list.append((expr, depth))

    return data_list 

def make_nodes(data_list):
    nodes = []
    for i in range(len(data_list)):
        nodes.append(ExprTree())
        nodes[i].expr = data_list[i][0]
        nodes[i].depth = data_list[i][1]
    return nodes

def make_tree(nodes):
    cursor = 0
    i = 1
    root = nodes[0]
    while i < len(nodes):
        if nodes[i].depth > nodes[cursor].depth:
            if not nodes[cursor].left:
                nodes[cursor].left = nodes[i]
                i += 1
                cursor = i - 1
            elif not nodes[cursor].right:
                nodes[cursor].right = nodes[i]
                i += 1
                cursor = i - 1
            else:
                print "Couldn't place node in tree because cursor already has two children."
                break
        else:
            cursor -= 1
    return root 

def parse_into_tree(FILE):
    lines = parse_lines(FILE)
    data_list = extract_lines(lines)
    nodes = make_nodes(data_list)
    tree = make_tree(nodes)
    print "Printing tree in bfs-order."
    bfs(tree)
    return tree
