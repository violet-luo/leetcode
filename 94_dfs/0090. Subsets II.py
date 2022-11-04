def subsetsWithDup(self, nums):
    res, subset = [], [] 
    nums = sorted(nums)  # 去重需要排序
    self.backtrack(nums, 0, res, subset)
    return res

def backtrack(self, nums, start_idx, res, subset):
    res.append(subset[:])
    for i in range(start_idx,len(nums)):
        if i > start_idx and nums[i] == nums[i - 1]:  # 跳过重复元素
            continue
        subset.append(nums[i])
        self.backtrack(nums, i + 1, res, subset) 
        subset.pop() 
