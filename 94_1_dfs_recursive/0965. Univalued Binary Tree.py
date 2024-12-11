def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
    uni_value = root.val

    def traverse(node):
        if not node:
            return True
        if node.val != uni_value:
            return False
        return traverse(node.left) and traverse(node.right)
    
    return traverse(root)
        
###

def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
    res = []

    def traverse(node):
        if not node:
            return
        res.append(node.val)
        traverse(node.left)
        traverse(node.right)
    
    traverse(root)
    return len(set(res)) == 1

###

def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    uni_value = root.val
    if root.left:
        if root.left.val != uni_value:
            return False
    if root.right:
        if root.right.val != uni_value:
            return False
    return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        
###

def isUnivalTree(self, root):
    if not root:
        return True
    if root.left:
        if root.left.val != root.val:
            return False
    if root.right:
        if root.right.val != root.val:
            return False
    return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
