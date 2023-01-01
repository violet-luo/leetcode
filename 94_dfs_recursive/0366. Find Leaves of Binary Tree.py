def findLeaves(self, root):
    res = collections.defaultdict(list)

    # 自底向上递归
    def getHeight(root):
        if not root:
            return 0

        left_height = getHeight(root.left)
        right_height = getHeight(root.right)
        height = max(left_height, right_height) + 1

        res[height].append(root.val)
        return height

    getHeight(root)
    return [v for v in res.values()]

###

def findLeaves(self, root):
    res = []
    self.depth = {}
    max_depth = self.getHeight(root)
    for i in range(1, max_depth + 1):
        res.append(self.depth.get(i))
    return res

def getHeight(self, root):
    if not root:
        return 0

    # 高度取决于两个子节点中的较大值
    left_height = self.getHeight(root.left)
    right_height = self.getHeight(root.right)
    height = 1 + max(left_height, right_height)

    if height not in self.depth:
        self.depth[height] = []
    self.depth[height].append(root.val)

    return height
