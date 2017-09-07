from src.parse import parse_into_tree 
from src.interpret import interpret
from src.format_pico import print_to_file

INPUT_FILE = "input/theorem.out"
OUT_FILE = "theorem.cnf"

tree = parse_into_tree(INPUT_FILE)
clauses, var_len = interpret(tree)
print_to_file(OUT_FILE, clauses, var_len)
