def twoSum6(nums, target):
    if not nums or len(nums) < 2:
        return 0
    
    count = 0
    nums.sort()
    l, r = 0, len(nums) - 1
    seen_pair = (None, None)
    
    while l < r:
        two_sum = nums[l] + nums[r]
        if two_sum == target:
            if (nums[l], nums[r]) != seen_pair:
                count += 1
            seen_pair = (nums[l], nums[r])
            l, r = l + 1, r - 1
        elif two_sum > target:
            r -= 1
        else:
            l += 1
    
    return count
