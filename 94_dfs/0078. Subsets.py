def subsets(self, nums):
    res, subset = [], []
    self.backtrack(nums, 0, res, subset)
    return res

def backtrack(self, nums, start_idx, res, subset):
    res.append(subset[:])
    for i in range(start_idx, len(nums)):
        subset.append(nums[i])
        self.backtrack(nums, i + 1, res, subset)
        subset.pop()
