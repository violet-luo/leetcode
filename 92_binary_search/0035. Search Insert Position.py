def searchInsert(nums, target):
    l, r = 0, len(nums) - 1
    
    # 标准二分模版
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid
        else:
            r = mid
    
    if nums[l] >= target: # [1,2], 0
        return l
    if nums[r] >= target: # [1,2], 1
        return r
    return len(nums) # [1, 2], 3
