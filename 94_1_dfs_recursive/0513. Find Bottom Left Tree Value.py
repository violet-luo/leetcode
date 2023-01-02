def findBottomLeftValue(self, root):
    self.res = None
    self.max_height = 0
    self.get_height(root, 1)
    return self.res
    
def get_height(self, root, height):
    if not root: 
        return
        
    if height > self.max_height:
        self.max_height = height
        self.res = root.val
        
    self.get_height(root.left, height + 1)
    self.get_height(root.right, height + 1)
