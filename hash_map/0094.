"""

1. Recursive
Runtime: 32 ms, faster than 53.64% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14 MB, less than 99.97% of Python3 online submissions for Binary Tree Inorder Traversal.

"""

def inorderTraversal1(self, root):
    res = []
    self.helper(root, res)
    return res

def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
        
        
"""

2. Iterative
Runtime: 32 ms, faster than 53.64% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14.2 MB, less than 99.97% of Python3 online submissions for Binary Tree Inorder Traversal.

"""

def inorderTraversal(self, root):
    res, stack = [], []

    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            res.append(tmpNode.val)
            root = tmpNode.right
    return res
