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

def permute(self, nums: List[int]) -> List[List[int]]:
    res, subset = [], []

    def backtrack(nums):
        if len(subset) == len(nums):
            res.append(subset[:]) 
            return
        for num in nums: # 因为是集合而不是组合，所以从0开始遍历
            # 去重，如果不去重，会得到[1, 1, 1]
            # 组合不用加去重这两行，因为组合是从start_index开始
            if num in subset: 
                continue
            subset.append(num)
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
