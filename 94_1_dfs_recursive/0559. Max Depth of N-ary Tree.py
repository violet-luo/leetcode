def maxDepth(self, root: 'Node') -> int:
    def get_height(node) -> int:
        if not node:
            return 0
        
        max_depth = 0
        for child in node.children:
            depth = get_height(child)
            max_depth = max(max_depth, depth)
        return 1 + max_depth
    
    return get_height(root)

###

def maxDepth(self, root):
    if not root:
        return 0
    depth = 0
    for child in root.children:
        depth = max(depth, self.maxDepth(child))
    return depth + 1
