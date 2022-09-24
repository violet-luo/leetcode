def verticalOrder(self, root):
    #defaultdict provides a default value for the key that does not exist
    res = collections.defaultdict(list) 
    queue = collections.deque([(root, 0)])

    while queue:
        node, pos = queue.popleft()
        if node:
            res[pos].append(node.val) # 每一个pos加入node
            queue.append((node.left, pos - 1))
            queue.append((node.right, pos + 1))
    
    return [res[i] for i in sorted(res)] # {-1: [9], 0: [3, 15], 1: [20], 2: [7]}
