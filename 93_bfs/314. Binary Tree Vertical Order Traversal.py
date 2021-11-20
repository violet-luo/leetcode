def verticalOrder(self, root):
    res = collections.defaultdict(list)
    queue = collections.deque([(root, 0)])

    while queue:
        node, x = queue.popleft()
        if node:
            res[x].append(node.val) # 每一个pos加入node
            queue.append((node.left, x - 1))
            queue.append((node.right, x + 1))
    
    return [res[i] for i in sorted(res)] # {0: [3, 15], -1: [9], 1: [20], 2: [7]}
