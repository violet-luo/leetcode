# 1. DFS递归
def inorderPredecessor(self, root, p):
    if root.val > p.val:
        return self.inorderPredecessor(root.left, p)
    elif root.val == p.val:
        return root.left
    else: # root.val < p.val
        node = self.inorderPredecessor(root.right, p)
        if not node:
            return root
        else:
            return node

# 2. DFS非递归
def inorderPredecessor(self, root, p):
    predecessor = None
    while root:
        if root.val >= p.val:
            root = root.left
        else:
            predecessor = root
            root = root.right
    return predecessor
