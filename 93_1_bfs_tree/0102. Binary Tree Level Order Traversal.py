def levelOrder(self, root):
    if not root:
        return []

    # 1. 把第一层的节点放到队列当中
    queue = collections.deque([root])
    results = []

    # 2. while 队列非空
    while queue:
        results.append([node.val for node in queue])
        # 3. 把上一层的节点拓展出下一层的节点
        for i in range(len(queue)):
            node = queue.popleft()
            # 如果有左儿子，把左儿子拿进来
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return results
