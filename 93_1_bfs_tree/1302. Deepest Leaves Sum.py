def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    res = collections.defaultdict(list)
    q = collections.deque([(root, 0)])

    while q:
        for i in range(len(q)):
            node, depth = q.popleft()
            res[depth].append(node.val)
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

    max_depth = max(res.keys())
    return sum(res[max_depth])
        
###

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
