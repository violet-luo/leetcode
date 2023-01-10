def sumRootToLeaf(self, root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    if root.left:
        root.left.val = root.val * 2 + root.left.val
    if root.right:
        root.right.val = root.val * 2 + root.right.val
    return self.sumRootToLeaf(root.left) + self.sumRootToLeaf(root.right)
    
###

def sumRootToLeaf(self, root):
    return self.helper(root, 0)

def helper(self, root, val):
    if not root: 
        return 0
    val = val * 2 + root.val # 二进制转换
    if not root.left and not root.right: 
        return val
    return self.helper(root.left, val) + self.helper(root.right, val)
