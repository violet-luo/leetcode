"""

1. Recursion
Runtime: 88 ms, faster than 43.83% of Python3 online submissions for Count Complete Tree Nodes.
Memory Usage: 21.4 MB, less than 100.00% of Python3 online submissions for Count Complete Tree Nodes.

"""

def countNodes(self, root: TreeNode) -> int:
    if root:
        return 1 + self.countNodes(root.right) + self.countNodes(root.left)
    return 0
