def permuteUnique(self, nums):
    if not nums: 
        return []
    res, subset = [], []
    seen = [False] * len(nums)
    self.backtrack(sorted(nums), seen, res, subset)
    return res

def backtrack(self, nums, seen, res, subset):
    if len(subset) == len(nums):
        res.append(subset[:])
        return

    for i in range(len(nums)):
        if seen[i] or (i > 0 and nums[i] == nums[i-1] and not seen[i-1]): # 元素已访问过或是重复元素
            continue
        seen[i] = True
        subset.append(nums[i])
        self.backtrack(nums, seen, res, subset)
        subset.pop()
        seen[i] = 0
