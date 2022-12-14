def findMode(self, root):
    res = {}
    self.dfs(root, res)
    mode = max(res.values())
    return [key for key in res.keys() if res[key] == mode]

def dfs(self, root, res):
    if not root:
        return
    if root.val not in res:
        res[root.val] = 1
    else:
        res[root.val] += 1
    self.dfs(root.left, res)
    self.dfs(root.right, res)
