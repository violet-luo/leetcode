def pathSum(self, root, targetSum):
    if not root:
        return 0
    # 2. 从该节点向下找存在的路径个数
    def dfs(root, targetSum):
        count = 0
        if not root:
            return 0
        if root.val == targetSum:
            count += 1
        count += dfs(root.left, targetSum - root.val)
        count += dfs(root.right, targetSum - root.val)
        return count
    # 1. 遍历每个节点
    return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
