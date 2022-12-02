def arrayPairSum(self, nums: List[int]) -> int:
    res = 0
    nums.sort()
    i = 0
    
    while i < len(nums):
        res += nums[i]
        i += 2
        
    return res
