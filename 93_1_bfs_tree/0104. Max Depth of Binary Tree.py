def maxDepth(self, root):
    if not root:
        return 0
    queue = collections.deque([(root, 1)])
    res = 0

    while queue:
        for _ in range(len(queue)):
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        res += 1
        
    return res
