def sumNumbers(self, root):
    return self.dfs(root, 0)

# 因为需要上一个节点的信息，所以需要重新建立一个dfs
def dfs(self, root, prev):
    if not root:
        return 0
    sum = root.val + prev * 10
    if not root.left and not root.right: # 出口
        return sum
    return self.dfs(root.left, sum) + self.dfs(root.right, sum)
