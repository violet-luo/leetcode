def findSecondMinimumValue(self, root):
    res = [float('inf')]
    def traverse(node):
        if not node:
            return
        if root.val < node.val < res[0]:
            res[0] = node.val
        traverse(node.left)
        traverse(node.right)
    traverse(root)
    return -1 if res[0] == float('inf') else res[0]

###

def findSecondMinimumValue(self, root):
    if not root or not root.left or not root.right:
        return -1
    # 左右子节点中不同于 root.val 的那个值可能是第二小的值
    l, r = root.left.val, root.right.val
    
    # 如果左右子节点都等于 root.val，则去左右子树递归寻找第二小的值
    if root.val == root.left.val:
        l = self.findSecondMinimumValue(root.left)
    if root.val == root.right.val:
        r = self.findSecondMinimumValue(root.right)
    if l == -1:
        return r
    if r == -1:
        return l
    # 如果左右子树都找到一个第二小的值，更小的那个是整棵树的第二小元素
    return min(l, r)

###

def findSecondMinimumValue(self, root):
    self.res = -1
    self.dfs(root, root.val)
    return self.res

def dfs(self, root, node):
    if not root:
        return
    if root.val != node:
        if self.res == -1:
            self.res = root.val
        else:
            self.res = Math.min(self.ans, root.val)
        return
    self.dfs(root.left, root.val)
    self.dfs(root.right, root.val)
