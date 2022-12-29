def subsets(self, nums):
    res, subset = [], []
        
    def backtrack(start_index):
        res.append(subset[:]) # 硬拷贝不能是res.append(subset)
        # 因为是组合不是集合，所以不是从0而是从start_index开始遍历
        for i in range(start_index, len(nums)):
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            
    backtrack(0)
    return res

###

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
