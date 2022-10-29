def maximumAverageSubtree(self, root) -> float:
    self.max_avg = 0
    self.dfs(root)
    return self.max_avg

def dfs(self, root):
    if not root:
        return 0, 0
    l_total, l_size = self.dfs(root.left)
    r_total, r_size = self.dfs(root.right)
    total = l_total + root.val + r_total
    size = l_size + 1 + r_size 
    self.max_avg = max(self.max_avg, total/size)
    return total, size
