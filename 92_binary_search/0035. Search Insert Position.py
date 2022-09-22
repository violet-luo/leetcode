def searchInsert(nums, target):
    l, r = 0, len(nums) - 1
    
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid
        else:
            r = mid
    
    if nums[l] >= target:
        return l
    if nums[r] >= target:
        return r
    return len(nums)
