def findSubTree(self, root)：
    self.max_sum = float('-inf')
    self.res = root
    self.get_sum(root)
    return self.res

def get_sum(self, root):
    if not root:
        return 0
    left = self.get_sum(root.left)
    right = self.get_sum(root.right)
    sum = root.val + left + right
    if sum > self.max_sum:
        self.max_sum = sum
        self.res = root
    return sum
