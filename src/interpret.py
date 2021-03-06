from bfs import bfs_script

bin_op = set(['<->', '->', '\/', '/\\'])
un_op = set(['|-', '=', '-.'])
# SHOULD BE VAR NAMES
var_expr = set(['ph', 'ps', 'ch', 'th', 'ta', 'et', 'ze', 'si', 'rh', 'mu', 'la', 'ka'])

def make_or_clause(x, a, b):
    or_clause = [
            (x, -a),
            (x, -b),
            (-x, a, b)
            ]
    return or_clause

def make_and_clause(x, a, b):
    and_clause = [
            (x, -a, -b),
            (-x, a),
            (-x, b)
            ]
    return and_clause

def make_iff_clause(x, a, b):
    iff_clause = [
        (x, a, b),
        (x, -a, -b),
        (-x, a, -b),
        (-x, -a, b)
        ]
    return iff_clause

def make_imp_clause(x, a, b):
    imp_clause = [
        (x, a),
        (x, -b), 
        (-x, -a, b)
        ]
    return imp_clause

def assign_var(node, assignment):
    i = len(assignment)
    assignment.update({node: i}) 

def print_assignment(node, assignment):
    print assignment[node]

# O(n^2) alg -- use hash table.
# could look this up into hash table 
# also can assign here in dfs way and restruct 
def clean_var_expr(var_node, current_node, assignment):
    if current_node.expr == var_node.expr:
        assignment[current_node] = assignment[var_node]
    else:
        if current_node.left:
            clean_var_expr(var_node, current_node.left, assignment)
        if current_node.right: 
            clean_var_expr(var_node, current_node.right, assignment)

def optimize(node, tree, assignment, var_expr_set):
    if node.expr in var_expr:
        if node.expr not in var_expr_set:
            var_expr_set.add(node.expr)
            clean_var_expr(node, tree, assignment)
            
    # go deep in that first case
    elif node.expr in un_op:
        assignment[node] = None
        optimize(node.left, tree,  assignment, var_expr_set)

        if node.expr == '-.':
            var = assignment[node.left]
            assignment.update({node.left: -var})
        
        elif node.expr == '|-':
            print "End of optimization."
            return assignment
        
    elif node.expr in bin_op:
        optimize(node.left, tree, assignment, var_expr_set)
        optimize(node.right, tree, assignment, var_expr_set)
    else: 
        raise ValueError("Could not parse expression " + node.expr + ".")

def reenumerate(assignment):
    old_vars = [] 
    for key in assignment:
        if assignment[key]:
            old_var = assignment[key]
            if abs(old_var) not in old_vars:
                old_vars.append(abs(old_var))

    old_vars = sorted(old_vars)
    n = len(old_vars) + 1
    new_vars = range(1, n)

    var_dict = {}
    for i in range(len(old_vars)):
        var_dict.update({old_vars[i]: new_vars[i]})
        
    # We rely on the fact that the keys appear in the order they were assigned in Python.
    for key in assignment:
        if assignment[key]:
            old_var = assignment[key]
            if old_var < 0:
                assignment[key] = -var_dict[-old_var]
            else:
                assignment[key] = var_dict[old_var]
    return assignment, n  

# the control flow should be based on whether or not we have un_op.
# mutate the tree here -- instead of optimize (which goes up-down) instead of down-up
# easier to read, and less worry. 
# name this get assignment. (this action is called assignment). 
def near_childvar(node, assignment):
    if assignment[node]:
        return assignment[node]
    else:
        return near_childvar(node.left, assignment)

# missing clauses to add (and and or)
# assignment is map 
def declare_clauses(assignment):
    # adds negation of our statement 
    clauses = [(-1,)]
    for node in assignment:
        if node.expr in bin_op:
            x = assignment[node]
            a = near_childvar(node.left, assignment)
            b = near_childvar(node.right, assignment)
            if node.expr == '<->':
                clauses.extend(make_iff_clause(x,a,b))
            elif node.expr == '->':
                clauses.extend(make_imp_clause(x,a,b))
    return clauses

# call bfs_script -> bfs_label
def interpret(tree):
    assignment = {}
    # closure = lambda node: assign_var(node, assignment) -- but not really how to
    # assignment = bfs...(tree, closure)
    # or the pythonic way to do is is to create a class (multiple funcs + a class)
    # assignment.assign_var (bound method)
    assignment = bfs_script(tree, assign_var, assignment, assignment)
    assignment = optimize(tree, tree, assignment, set([]))
    assignment, var_num = reenumerate(assignment)
    
    print "Printing assignment."
    print assignment 

    clauses = declare_clauses(assignment)
    print "Printing clauses."
    print clauses

    return clauses, var_num
    
