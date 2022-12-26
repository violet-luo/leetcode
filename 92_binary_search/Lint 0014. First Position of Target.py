def binary_search(nums, target): #[1,2,2,2,3],2
    if not nums or not target:
        return -1
    l, r = 0, len(nums)-1
    
    while l + 1 < r :
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid
        elif nums[mid] > target:
            r = mid
        else:
            r = mid # 如果遇到2，做右边界，找第一个

    # 循环结束时，l 和 r 的关系是相邻关系
    # 坑2：需要再单独判断 l 和 r 这两个数谁是我们要的答案
    # 如果是找 first position of target 就先看 l，否则就先看 r
    if nums[l] == target:
        return l
    elif nums[r] == target:
        return r
    return -1
