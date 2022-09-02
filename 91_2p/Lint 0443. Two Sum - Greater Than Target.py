def twoSum2(self, nums, target):
    n = len(nums)
    if not nums or n < 2:
        return 0
    
    nums.sort()
   count = 0
    l, r = 0, n - 1
    
    while l < r:
        if nums[l] + nums[r] <= target:
            l += 1
        else:
            count += r - l
            r -= 1
            
    return count
