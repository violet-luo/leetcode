def findMode(self, root):
    res = collections.defaultdict(int)
    self.dfs(root, res)
    mode = max(res.values())
    return [key for key in res.keys() if res[key] == mode]

def dfs(self, root, res):
    if not root:
        return
    res[root.val] += 1
    self.dfs(root.left, res)
    self.dfs(root.right, res)
