def buildTree(self, preorder, inorder):
    if not inorder:
       return
    root = TreeNode(preorder[0]) # 前序的第一个数为根
    root_idx = inorder.index(preorder[0]) # 在中序中找到根的位置，不知道为什么这里改成root就会报错
    root.left = self.buildTree(preorder[1 : root_idx + 1], inorder[ : root_idx])
    root.right = self.buildTree(preorder[root_idx + 1 : ], inorder[root_idx + 1 : ])
    return root
