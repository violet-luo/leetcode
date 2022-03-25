def countNodes(self, root):
    l_depth = self.getHeight(root, True)
    r_depth = self.getHeight(root, False)

    if l_depth == r_depth:
        return 2 ** l_depth - 1
    else:
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

def getHeight(self, root, isLeft):
    if root is None:
        return 0
    if isLeft:
        return 1 + self.getHeight(root.left, isLeft)
    else:
        return 1 + self.getHeight(root.right, isLeft)
