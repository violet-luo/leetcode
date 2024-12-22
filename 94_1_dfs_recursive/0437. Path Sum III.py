def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    cnt = 0

    def traverse(node, path) -> None:
        nonlocal cnt
        if not node:
            return None
        
        path.append(node.val)
        cur_sum = 0
        # Traverse path in reverse to consider all sub-paths ending at the current node
        for i in range(len(path) - 1, -1, -1):  
            cur_sum += path[i]
            if cur_sum == targetSum:
                cnt += 1

        traverse(node.left, path)
        traverse(node.right, path)

        path.pop()
    
    traverse(root, [])

    return cnt

###

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
