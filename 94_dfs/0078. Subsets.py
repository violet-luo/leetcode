def subsets(self, nums):
    self.res, self.subset = [], []
    self.backtrack(nums, 0)
    return self.res

def backtrack(self, nums, start_idx):
    self.res.append(self.subset[:])
    for i in range(start_idx, len(nums)):
        self.subset.append(nums[i])
        self.backtrack(nums, i + 1)
        self.subset.pop()
