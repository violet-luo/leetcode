def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    cnt = 0
    
    # 记录前缀和出现次数的哈希表
    prefix_sum_count = defaultdict(int)
    # 初始化前缀和为 0 出现 1 次，表示从根节点到某个节点的路径和为 targetSum 时的起点
    prefix_sum_count[0] = 1
    
    def traverse(node, current_sum):
        nonlocal cnt
        if node is None:
            return
        
        current_sum += node.val
        
        # 如果 current_sum - targetSum 在哈希表中出现过，说明找到了符合条件的路径
        cnt += prefix_sum_count[current_sum - targetSum]
        
        # 将当前路径和加入哈希表，表示当前路径和出现一次
        prefix_sum_count[current_sum] += 1
        
        traverse(node.left, current_sum)
        traverse(node.right, current_sum)
        
        prefix_sum_count[current_sum] -= 1
    
    # 从根节点开始遍历，初始路径和为 0
    traverse(root, 0)
    
    return cnt
