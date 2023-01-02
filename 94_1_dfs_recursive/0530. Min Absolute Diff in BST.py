def getMinimumDifference(self, root):
    def inorder(root):
        if not root:
            return

        inorder(root.left) # 先遍历左子树
        self.min_diff = min(self.min_diff, abs(self.pre - root.val)) # 记录当前节点和前一个节点的差值
        self.pre = root.val # 当前节点遍历之后就变成了前一个节点
        inorder(root.right) # 再遍历右子树

    self.min_diff, self.pre = float('inf'), float('inf')
    inorder(root)
    return self.min_diff

###

def getMinimumDifference(self, root):
    self.res = float('inf')
    self.pre = None
    self.inorder(root)
    return self.res

def inorder(self, node):
    if not node:
        return

    self.inorder(node.left)
    if self.pre is not None:
        self.res = min(self.res, node.val - self.pre)

    self.pre = node.val
    if node.right: 
        self.inorder(node.right)
