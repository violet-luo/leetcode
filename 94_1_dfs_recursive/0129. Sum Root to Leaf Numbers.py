def sumNumbers(self, root: Optional[TreeNode]) -> int:
    res = 0

    def traverse(node, path: string) -> None:
        nonlocal res
        if not node:
            return None
        
        path += str(node.val)
        if not node.left and not node.right:
            res += int(path)
        else:
            traverse(node.left, path)
            traverse(node.right, path)
    
    traverse(root, '')
    return res

###

def sumNumbers(self, root: Optional[TreeNode]) -> int:
    res = 0

    def traverse(node, path_sum):
        nonlocal res
        if not node:
            return None

        path_sum += node.val
        if not node.left and not node.right:
            res += path_sum
        else:
            path_sum *= 10
            traverse(node.left, path_sum)
            traverse(node.right, path_sum)

    traverse(root, 0)
    return res
        
###

def sumNumbers(self, root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    if root.left:
        root.left.val = root.val * 10 + root.left.val
    if root.right:
        root.right.val = root.val * 10 + root.right.val
    return self.sumNumbers(root.left) + self.sumNumbers(root.right)

###

def sumNumbers(self, root):
    return self.helper(root, 0)

# 因为需要上一个节点的信息，所以需要重新建立一个helper
def helper(self, root, prev):
    if not root:
        return 0
    sum = root.val + prev * 10
    if not root.left and not root.right: # 出口
        return sum
    return self.helper(root.left, sum) + self.helper(root.right, sum)
