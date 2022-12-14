def findSubTree(self, root)：
    self.min_sum = float('inf')
    self.res = root
    self.get_sum(root)
    return self.res

def get_sum(self, root):
    if not root:
        return 0
    left = self.get_sum(root.left)
    right = self.get_sum(root.right)
    sum = root.val + left + right
    if sum < self.min_sum:
        self.min_sum = sum
        self.res = node
    return sum
