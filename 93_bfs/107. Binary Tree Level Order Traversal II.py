def levelOrder(self, root):
    if not root:
        return []

    # 1. 把第一层的节点放到队列当中，先进先出，deque是双头queue, 头尾都可以push或pop
    queue = collections.deque([root]) # 而不是 from collections import deque
    res = []

    # 2. while 队列非空
    while queue:
        level = []
        # 3. 把上一层的节点拓展出下一层的节点
        for i in range(len(queue)): #traverse当前层结点
            node = queue.popleft()
            level.append(node.val)
            # 如果有左儿子，把左儿子拿进来
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res[::-1]
