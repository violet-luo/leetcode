def inorderSuccessor(self, root, p):
    if not root:
        return

    if root.val <= p.val:
        return self.inorderSuccessor(root.right, p)
    else:
        node = self.inorderSuccessor(root.left, p)
        if not node: 
            return root
        else:
            return node


##

def inorderPredecessor(self, root, p):
    predecessor = None
    
    while root:
        if root.val >= p.val:
            root = root.left
        else:
            predecessor = root
            root = root.right
    
    return predecessor
