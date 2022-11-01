def deepestLeavesSum(self, root):
    self.res = 0
    self.max_level = -1
    self.dfs(root, 0)
    return self.res

def dfs(self, root, level):
    if not root:
        return

    if level > self.max_level:
        self.max_level = level 
        self.res = root.val
    elif level == self.max_level:
        self.res += root.val

    self.dfs(root.left, level + 1)
    self.dfs(root.right, level + 1)
