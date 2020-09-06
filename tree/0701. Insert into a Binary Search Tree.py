"""

Runtime: 144 ms, faster than 73.10% of Python3 online submissions for Insert into a Binary Search Tree.
Memory Usage: 16 MB, less than 36.83% of Python3 online submissions for Insert into a Binary Search Tree.

"""

def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    return self.traverse(root, val)

def traverse(self, root, val):
    if root is None:
        return TreeNode(val)
    if root.val > val:
        root.left = self.traverse(root.left, val)
    else:
        root.right = self.traverse(root.right, val)
    return root
