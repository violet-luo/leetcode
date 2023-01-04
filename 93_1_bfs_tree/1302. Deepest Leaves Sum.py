def deepestLeavesSum(self, root):
    queue = collections.deque([root])
    while queue:
        res = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            res += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res
