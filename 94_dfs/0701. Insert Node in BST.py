def insertNode(self, root, node):
    return self.traverse(root, node)
    
def traverse(self, root, node):
    if root is None:
        return node
    if root.val > node.val:
        root.left = self.traverse(root.left, node)
    else:
        root.right = self.traverse(root.right, node)
    return root
