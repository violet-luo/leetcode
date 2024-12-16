def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
    min_val = root.val
    second_min_val = float('inf')
    
    def traverse(node) -> None:
        nonlocal second_min_val
        if not node:
            return None
        
        if min_val < node.val < second_min_val:
            second_min_val = node.val
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return second_min_val if second_min_val != float('inf') else -1

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
