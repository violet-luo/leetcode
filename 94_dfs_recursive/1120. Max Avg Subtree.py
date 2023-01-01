def maximumAverageSubtree(self, root):
    max_avg = float('-inf')

    def get_sum(root):
        if not root:
            return 0, 0
        l_sum, l_size = get_sum(root.left)
        r_sum, r_size = get_sum(root.right)
        sum = l_sum + root.val + r_sum
        size = l_size + 1 + r_size 
        nonlocal max_avg
        max_avg = max(max_avg, sum/size)
        return sum, size

    get_sum(root)
    return max_avg

##

def maximumAverageSubtree(self, root):
    self.max_avg = float('-inf')
    self.get_sum(root)
    return self.max_avg

def get_sum(self, root):
    if not root:
        return 0, 0
    l_sum, l_size = self.get_sum(root.left)
    r_sum, r_size = self.get_sum(root.right)
    sum = l_sum + root.val + r_sum
    size = l_size + 1 + r_size 
    self.max_avg = max(self.max_avg, sum/size)
    return sum, size
