def two_sum5(self, nums, target):
    n = len(nums)
    if not nums or n < 2:
        return 0
        
    nums.sort()
    count = 0
    left, right = 0, n - 1
    
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        else:
            count += right - left
            left += 1
            
    return count
