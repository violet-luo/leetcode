def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 0
    
    left_sum = 0
    q = collections.deque([root])
    while q:
        node = q.popleft()
        if not node.left and not node.right:
            left_sum += node.val
        if node.left:
            q.append(node.left)
        if node.right:
            node.right.val = 0
            q.append(node.right)
    
    return left_sum

###

def sumOfLeftLeaves(self, root):
    queue = collections.deque([root])
    res = 0
    while queue:
        node = queue.popleft()
        if node.left and not node.left.left and not node.left.right: # 走到左叶子
            res += node.left.val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res
