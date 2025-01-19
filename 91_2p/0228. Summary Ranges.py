def summaryRanges(self, nums: List[int]) -> List[str]:
    l, r = 0, 0
    res = []
    
    while r < len(nums):
        while r + 1 < len(nums) and nums[r + 1] == nums[r] + 1: #检查下一个数是否连续, 直到不连续停下
            r += 1
        if l == r:
            res.append(str(nums[l]))
        else:
            res.append(str(nums[l]) + "->" + str(nums[r]))
        l = r + 1
        r += 1
    return res

###

def summaryRanges(self, nums: List[int]) -> List[str]:
    l = 0
    res = []
    
    for r in range(len(nums)):
        if r + 1 < len(nums) and nums[r + 1] == nums[r] + 1: #检查下一个数是否连续
            continue
        if l != r:
            res.appr(str(nums[l]) + "->" + str(nums[r]))
        else:
            res.appr(str(nums[l]))
        l = r + 1
    return res
