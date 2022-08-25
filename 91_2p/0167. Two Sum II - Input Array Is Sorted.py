def twoSum(nums, target):
    if not nums:
        return [-1, -1]
    
    l, r = 0, len(nums) - 1
    
    while l < r:
        two_sum = nums[l] + nums[r]
        if two_sum == target:
            return [l+1, r+1] # 1-indexed
        elif two_sum < target:
            l += 1
        else:
            r -= 1
