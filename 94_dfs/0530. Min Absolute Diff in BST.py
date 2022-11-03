def getMinimumDifference(self, root):
    self.res = float('inf')
    self.pre = None
    self.inorder(root)
    return self.res

def inorder(self, node):
    if not node:
        return

    self.inorder(node.left)
    if self.pre is not None:
        self.res = min(self.res, node.val - self.pre)

    self.pre = node.val
    if node.right: 
        self.inorder(node.right)
