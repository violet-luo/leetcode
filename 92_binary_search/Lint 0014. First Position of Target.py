def firstPosition(nums, target):
    # 通用二分模板
    if not nums or not target:
        return -1
    l, r = 0, len(nums) - 1
    
    while l + 1 < r :
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid
        else:
            r = mid
    
    if nums[l] == target:
        return l
    elif nums[r] == target:
        return r
    return -1
