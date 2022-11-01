def connect(self, root):
    if not root:
        return
    
    left, right = root.left, root.right
    
    while left and right:
        left.next = right
        left, right = left.right, right.left
    
    self.connect(root.left)
    self.connect(root.right)
    
    return root
