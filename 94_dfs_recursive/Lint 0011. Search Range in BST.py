def searchRange(self, root, low, high):
    res = []
    self.dfs(root, low, high, res)
    return res

def dfs(self, root, low, high, res):
    if not root:
        return
    # 剪枝，如果当前节点小于等于low，不必访问左子树
    if root.val > low:
        self.dfs(root.left, low, high, res)
    # 剪枝，如果当前节点大于等于high，不必访问右子树
    elif root.val < high:
        self.dfs(root.right, low, high, res)
    else: #low <= root.val and root.val <= high
        res.append(root.val)
