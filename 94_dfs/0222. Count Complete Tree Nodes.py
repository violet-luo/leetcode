def invertTree(self, root):
    if not root:
        return
    root.left = self.invertTree(root.right)
    root.right = self.invertTree(root.left)
    return root
