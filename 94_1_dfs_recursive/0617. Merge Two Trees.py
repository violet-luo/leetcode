def mergeTrees(self, root1, root2):
    if not root2:
        return root1
    if not root1:
        return root2
    root3 = TreeNode(root1.val + root2.val)
    root3.left = self.mergeTrees(root1.left, root2.left)
    root3.right = self.mergeTrees(root1.right, root2.right)
    return root3
