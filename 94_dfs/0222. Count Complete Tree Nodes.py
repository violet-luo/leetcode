def countNodes(self, root):
    if not root:
        return 0
    return self.countNodes(root.left) + self.countNodes(root.right) + 1
