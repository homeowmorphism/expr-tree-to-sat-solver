# format for picosat

def align_clause(clause):
    str_clause = str(clause[0])
    for i in range(1, len(clause)):
        str_clause += " " + str(clause[i])
    str_clause += " 0"
    return str_clause

def print_to_file(filename, clauses, var_len):
    with open(filename, "w") as f:
        f.write("p cnf " + str(var_len) + " " + str(len(clauses)))
    with open(filename, "a") as f:
        for clause in clauses:
            str_clause = align_clause(clause)
            f.write("\n" + str_clause)

