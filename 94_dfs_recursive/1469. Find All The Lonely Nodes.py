def getLonelyNodes(self, root):
    res = []
    self.dfs(root, res)
    return res

# 因为需要多传一个参数，所以需要新建一个dfs
def dfs(self, root, res):
    if not root: #不能省略
        return
    if root.left and not root.right:
        res.append(root.left.val)
    if not root.left and root.right:
        res.append(root.right.val)
    self.dfs(root.left, res)
    self.dfs(root.right, res)
