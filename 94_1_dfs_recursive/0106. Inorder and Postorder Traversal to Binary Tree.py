def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if not inorder:
        return None
    
    root_val = postorder[-1]
    root = TreeNode(root_val) # 后序的最后一个为根
    root_idx = inorder.index(root_val) # 在中序中找到根的位，不知道为什么这里改成root就会报错    
    
    root.left = self.buildTree(inorder[ : root_idx], postorder[ : root_idx])
    root.right = self.buildTree(inorder[root_idx + 1 : ], postorder[root_idx : -1]) 
    return root
