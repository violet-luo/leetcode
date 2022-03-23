def inorderSuccessor(self, root, p):
    if not root:
        return
   # 根节点小于p，进入右子树递归
    if root.val <= p.val:
        return self.inorderSuccessor(root.right, p)
   # 根节点大于p, 进入左子树递归
    left = self.inorderSuccessor(root.left, p)
   
   # 如果是null, 直接返回当前节点
    if not left: 
        return root
   # 如果不是null, 返回左子树递归查找的结果
    else:
        return left
