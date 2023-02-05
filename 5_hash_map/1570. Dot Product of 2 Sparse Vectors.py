def __init__(self, nums):
    self.nums = {}
    for i, n in enumerate(nums):
        if n != 0:
            self.nums[i] = n

def dotProduct(self, vec):
    res = 0
    cur = vec.nums if len(vec.nums) < len(self.nums) else self.nums
    test = vec.nums if len(vec.nums) >= len(self.nums) else self.nums
    for i, n in cur.items():
        if i in test:
            res += n * test[i]
    return res
