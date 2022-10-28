def buildTree(self, inorder, postorder):
    if not inorder:
        return   
    root = TreeNode(postorder[-1]) # 后序的最后一个为根
    root_idx = inorder.index(postorder[-1]) # 在中序中找到根的位    
    root.left = self.buildTree(inorder[ : root_idx], postorder[ : root_idx])
    root.right = self.buildTree(inorder[root_idx + 1 : ], postorder[root_idx : -1]) 
    return root
