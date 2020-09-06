"""

Runtime: 40 ms, faster than 93.97% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.2 MB, less than 51.63% of Python3 online submissions for Validate Binary Search Tree.

"""

def isValidBST(self, root):
    return self.check_bst(root, float("-inf"), float("inf"))

def check_bst(self, node, left, right):
    if not node:
        return True
    if not left < node.val < right:
        return False
    return self.check_bst(node.left, left, node.val) and self.check_bst(node.right, node.val, right)
