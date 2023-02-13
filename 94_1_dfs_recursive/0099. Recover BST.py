def recoverTree(self, root):
    if not root:
        return
    self.pre, self.first, self.second = None, None, None
    self.dfs(root)
    if self.first:
        self.first.val, self.second.val = self.second.val, self.first.val
    return root

def dfs(self, root):
    if not root:
        return

    # 前序遍历，所得数字从小到大排序
    self.dfs(root.left) # 走到最左叶子
    if self.pre:
        if not self.first and self.pre.val > root.val: # 第一次碰到
            self.first = self.pre
        if self.first and self.pre.val > root.val: # 第二次碰到
            self.second = root
    self.pre = root
    self.dfs(root.right)
