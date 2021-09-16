def findSubtree(self, root):
    self.minimum_weight = float('inf')
    self.minimum_subtree_root = None
    self.getTreeSum(root)

    return self.minimum_subtree_root

# 得到root为根的二叉树的所有节点之和    
# 顺便打个擂台求出 min subtree
def getTreeSum(self, root):
    if root is None:
        return 0

    left_weight = self.getTreeSum(root.left)
    right_weight = self.getTreeSum(root.right)
    root_weight = left_weight + right_weight + root.val 

    if root_weight < self.minimum_weight:
        self.minimum_weight = root_weight
        self.minimum_subtree_root = root

    return root_weight
