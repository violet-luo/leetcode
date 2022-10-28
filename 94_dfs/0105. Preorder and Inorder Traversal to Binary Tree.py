def buildTree(self, preorder, inorder):
    if not inorder:
       return
    root = TreeNode(preorder[0]) # 前序的第一个数为根
    rootPos = inorder.index(preorder[0]) # 在中序中找到根的位置
    root.left = self.buildTree(preorder[1 : 1 + rootPos], inorder[ : rootPos])
    root.right = self.buildTree(preorder[rootPos + 1 : ], inorder[rootPos + 1 : ])
    return root
