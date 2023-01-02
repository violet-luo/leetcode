def find_subtree(self, root):
    min_sum = float('inf')
    res = root

    def get_sum(root):
        if not root:
            return 0
        left = get_sum(root.left)
        right = get_sum(root.right)
        sum = root.val + left + right
        nonlocal min_sum, res
        if sum < min_sum:
            min_sum = sum
            res = root
        return sum

    get_sum(root)
    return res

###

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
        self.res = root
    return sum
