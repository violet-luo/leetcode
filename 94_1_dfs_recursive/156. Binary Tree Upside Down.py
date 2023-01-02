def upsideDownBinaryTree(self, root):
    if not root or not root.left:
        return root
    new_left, new_right = root.left, root.right
    res = self.upsideDownBinaryTree(root.left)
    root.left = root.right = None
    new_left.left = new_right
    new_left.right = root
    return res
    
###

def upsideDownBinaryTree(self, root):
    if not root:
        return None
    return self.dfs(root)
    
def dfs(self, cur):
    if not cur.left:
        return cur
    
    new_root = TreeNode(cur.left)
    new_root = self.dfs(cur.left)
    
    cur.left.right = cur
    cur.left.left = cur.right
    cur.left = None
    cur.right = None
   return new_root
