def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
    res = 0
    
    def traverse(node, path_sum):
        nonlocal res
        if not node:
            return None
    
        path_sum += node.val
        if not node.left and not node.right:
            res += path_sum
        else:
            path_sum *= 2
            traverse(node.left, path_sum)
            traverse(node.right, path_sum)
    
    traverse(root, 0)
    return res
        
###

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
