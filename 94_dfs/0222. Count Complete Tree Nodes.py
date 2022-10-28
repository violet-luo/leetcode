def countNodes(self, root):
    if root == None:
        return 0

    leftHeight = self.getHeight(root.left)
    rightHeight = self.getHeight(root.right)
    
    # 如果左子树的深度 = 右子树的深度，左子树为满二叉树
    # 节点数 = 左子树的深度 + 右子树的深度 + 根节点
    if leftHeight == rightHeight:
        return (2 ** leftHeight - 1) + self.countNodes(root.right) + 1
    # 如果左子树的深度 ＞ 右子树的深度，右子树为满二叉树
    # 节点数 = 左子树的深度 + 右子树的深度 + 根节点
    else:
        return (2 ** rightHeight - 1) + self.countNodes(root.left) + 1

def getHeight(self, root:TreeNode):
    height = 0
    while root:
        root = root.left
        height += 1

    return height
