def kthfloorNode(self, root, k):
    if not root:
        return 0

    queue = collections.deque([root])

    while queue:
        if k == 1:
            return len(queue)
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        k -= 1
