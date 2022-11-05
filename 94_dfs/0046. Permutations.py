def permute(self, nums):
    res, subset = [], [] 
    self.backtrack(nums, res, subset)
    return res

def backtrack(self, nums, res, subset):
    if len(subset) == len(nums): #递归出口
        return res.append(subset[:]) 
    for i in range(len(nums)):
        if nums[i] in subset:  #subset里已经收录的元素，直接跳过
            continue
        subset.append(nums[i])
        self.backtrack(nums, res, subset) 
        subset.pop() 
