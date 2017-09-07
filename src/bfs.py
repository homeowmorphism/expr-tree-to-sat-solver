def bfs_internal(tree, visit, script, script_mem, ret):
    if not visit:
        visit = [tree]
    while visit:
        if tree.left not in visit:
            visit.append(tree.left)

        if tree.right not in visit:
            visit.append(tree.right)

        x = visit.pop(0)

        if x:
            script(x, script_mem)
            return bfs_internal(x, visit, script, script_mem, ret)
    return ret

def print_expr_node(node, mem = None):
    print (node.expr, node.depth)

def bfs(tree):
    bfs_internal(tree, [tree], print_expr_node, None, None) 

def bfs_script(tree, script, mem, ret):
   return bfs_internal(tree, [tree], script, mem, ret)
