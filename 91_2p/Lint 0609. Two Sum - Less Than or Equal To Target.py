def twoSum5(nums, target):
    n = len(nums)
    if not nums or n < 2:
        return 0
        
    nums.sort()
    count = 0
    l, r = 0, n - 1
    
    while l < r：
        two_sum = nums[l] + nums[r]
        if two_sum > target:
            r -= 1
        else:
            count += 1
            l += 1
    return count
