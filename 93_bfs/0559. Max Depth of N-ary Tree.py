def maxDepth(self, root):
    if not root:
        return 0
    queue = collections.deque([(root, 1)])
    while queue:
        node, level = queue.popleft()
        if node.children:
            for child in node.children:
                queue.append((child, level + 1))
    return level
