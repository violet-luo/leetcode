def kthSmallest(self, root, k):
    self.array = []
    self.dfs(root)
    return self.array[k - 1]

# 中序遍历
def dfs(self, root):
    if not root:
        return
    self.dfs(root.left)
    self.array.append(root.val)
    self.dfs(root.right)
