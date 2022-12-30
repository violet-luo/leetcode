def connect(self, root):
    if not root:
        return None
    queue = [root]
    while queue:
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if i == n - 1:
                break
            node.next = queue[0]
    return root
