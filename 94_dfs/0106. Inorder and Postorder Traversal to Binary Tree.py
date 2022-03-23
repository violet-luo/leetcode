def buildTree(self, inorder, postorder):
    if not inorder or len(inorder) == 0:
        return None
    
    root = TreeNode(postorder[-1]) # 后序的最后一个为根
    root_index = inorder.index(postorder[-1]) # 在中序中找到根的位置
    
    root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
    root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:-1])
    
    return root
