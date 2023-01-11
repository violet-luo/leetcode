def minDepth(self, root):
    if not root:
        return 0
        
    queue = collections.deque([(root, 1)])
    while queue:
        node, level = queue.popleft()
        if not node.left and not node.right: # 走到第一个叶子节点
            return level
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
