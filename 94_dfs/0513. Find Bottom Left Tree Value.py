def findBottomLeftValue(self, root):
    self.max_level = 0
    self.val = None
    self.getLevel(root, 1)
    return self.val
    
def getLevel(self, root, level):
    if not root: return
    if level > self.max_level:
        self.max_level = level
        self.val = root.val
    self.getLevel(root.left, level + 1)
    self.getLevel(root.right, level + 1)
