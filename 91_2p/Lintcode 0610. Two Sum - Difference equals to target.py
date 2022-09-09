def twoSum7(nums, target):
    target = abs(target)
    l, r = 0, 1
    while r < len(nums):
        if l == r:
            r += 1
        if nums[r] - nums[l] > target:
            l += 1
        elif nums[r] - nums[l] < target:
            r += 1
        else:
            return [nums[l], nums[r]]
    return [-1, -1]
