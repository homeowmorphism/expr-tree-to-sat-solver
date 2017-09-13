# expr should be "op" for operator

class ExprTree:
    def __init__(self, expr = None, depth = None, left = None, right = None):
        self.expr = expr
        self.depth = depth
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str((self.expr, self.depth))

    def __str__(self):
        return str((self.expr, self.depth))

    def height(self):
        if not self.left and not self.right:
            return 0
        elif not self.left:
            return self.right.height() + 1
        elif not self.right:
            return self.left.height() + 1
        else:
            return max(self.left.height(),  self.right.height()) + 1
