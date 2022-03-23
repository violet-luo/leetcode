def findLeaves(self, root):
    leaves = []
    self.getHeight(root, leaves)
    return leaves

# 返回节点的高度
def getHeight(self, root, leaves):
    if root is None:
        return -1
    
    height = -1
    
    # 高度取决于两个子节点中的较大值
    height = max(height, self.getHeight(root.left, leaves) + 1)
    height = max(height, self.getHeight(root.right, leaves) + 1)
    
    # 如果高度过大的话，往leaves中再加一个数组
    if height >= len(leaves):
        leaves.append([])
    
    leaves[height].append(root.val)
    
    return height
