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
