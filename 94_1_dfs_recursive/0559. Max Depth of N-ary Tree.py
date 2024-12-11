def maxDepth(self, root):
    def get_height(node):
        if node is None: 
            return 0
        elif not node.children:
            return 1
        else:
            height = [get_height(child) for child in node.children]
            return max(height) + 1
    return get_height(root)

###

def maxDepth(self, root):
    if root is None: 
        return 0 
    elif root.children == []:
        return 1
    else: 
        height = [self.maxDepth(c) for c in root.children]
        return max(height) + 1 
    
###

def maxDepth(self, root):
    if not root:
        return 0
    depth = 0
    for child in root.children:
        depth = max(depth, self.maxDepth(child))
    return depth + 1
