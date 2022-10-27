def lca(self, root, A, B):
    if not root:
        return None
    if root == A or root == B:
        return root 
    
    # 找 A 和 B
    left = self.lca(root.left, A, B)
    right = self.lca(root.right, A, B)

    # A 和 B 一边一个
    if left and right: 
        return root
    
    # 左子树有一个点或者左子树有LCA
    if left:
        return left
    
    # 右子树有一个点或者右子树有LCA
    if right:
        return right
        
    # 左右子树啥都没有
    return None
