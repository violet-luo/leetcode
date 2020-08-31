"""

Runtime: 44 ms, faster than 68.75% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.3 MB, less than 73.72% of Python3 online submissions for Maximum Depth of Binary Tree.

"""

def maxDepth(self, root):
    if root is None:
        return 0
    leftDepth = self.maxDepth(root.left)
    rightDepth = self.maxDepth(root.right)
    return max(leftDepth, rightDepth) + 1
