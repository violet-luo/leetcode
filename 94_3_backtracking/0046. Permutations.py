def permute(self, nums: List[int]) -> List[List[int]]:
    if not nums:
        return [[]]
        
    res, permutation = [], []

    def backtrack(nums, visited):
        if len(nums) == len(permutation):
            res.append(permutation[:])
            return
        
        for num in nums:
            if num in visited:
                continue
            permutation.append(num)
            visited.add(num)
            backtrack(nums, visited)
            visited.remove(num)
            permutation.pop()
    
    backtrack(nums, set())
    return res

###

def permute(self, nums):
    res = []
    subset = []

    def backtrack(nums):
        if len(subset) == len(nums):
            return res.append(subset[:]) 
        for i in range(len(nums)): #因为是集合而不是组合，所以从0开始遍历
            if nums[i] in subset: #去重
                continue
            subset.append(nums[i])
            backtrack(nums)
            subset.pop()

    backtrack(nums)
    return res

###

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
