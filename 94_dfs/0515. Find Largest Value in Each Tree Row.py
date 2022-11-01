def largestValues(self, root):
    self.res = []
    self.dfs(root, 0)
    return self.res

def dfs(self, root, height):
    if not root:
        return 

    # 如果相等等于这一层还没有节点放入res数组，所以把先序遍历遇到的第一个放入res数组
    if len(self.res) == height:
        self.res.append(root.val)
    else:
        self.res[height] = max(self.res[height], root.val)

    self.dfs(root.left, height + 1)
    self.dfs(root.right, height + 1)
