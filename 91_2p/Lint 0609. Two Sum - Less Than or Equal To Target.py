def twoSum5(nums, target):
    count = 0
    nums.sort()
    l, r = 0, len(nums) - 1
    
    while l < r：
        two_sum = nums[l] + nums[r]
        if two_sum > target:
            r -= 1
        else:
            count += 1
            l += 1
    return count
