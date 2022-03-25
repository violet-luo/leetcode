def searchRange(self, root, k1, k2):
    result = []
    self.dfs(root, k1, k2, result)
    return result

def dfs(self, root, k1, k2, result):
    if root is None:
        return
    if root.val > k1:
        self.dfs(root.left, k1, k2, result)
    if k1 <= root.val and root.val <= k2:
        result.append(root.val)
    if root.val < k2:
        self.dfs(root.right, k1, k2, result)
