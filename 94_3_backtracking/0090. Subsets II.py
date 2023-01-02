def subsetsWithDup(self, nums):
    res, subset = [], []
    nums = sorted(nums) #去重需要排序

    def backtrack(start_index):
        res.append(subset[:]) # 不能是res.append(subset)
        # 因为是组合不是集合，所以不是从0而是从start_index开始遍历
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]: # 与78区别，去重
                continue
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()

    backtrack(0)
    return res

###

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
