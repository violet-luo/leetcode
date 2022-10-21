def searchRange(self, root, k1, k2):
    res = []
    self.dfs(root, k1, k2, res)
    return res

def dfs(self, root, k1, k2, res):
    if not root:
        return
    # 剪枝，如果当前节点小于等于k1，不必访问左子树
    if root.val > k1:
        self.dfs(root.left, k1, k2, res)
    if k1 <= root.val and root.val <= k2:
        res.append(root.val)
    # 剪枝，如果当前节点大于等于k2，不必访问右子树
    if root.val < k2:
        self.dfs(root.right, k1, k2, res)
