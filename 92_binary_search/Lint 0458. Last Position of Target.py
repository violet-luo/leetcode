def lastPosition(nums, target):
    if not nums or not target:
        return -1 
    l, r = 0, len(nums) - 1

    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid
        elif nums[mid] > target:
            r = mid
        else:
            l = mid

    # 循环结束时，l 和 r 的关系是相邻关系
    # 坑2：需要再单独判断 l 和 r 这两个数谁是我们要的答案
    # 如果是找 last position of target 就先看 r，否则就先看 l
    if nums[r] == target:
        return r
    elif nums[l] == target:
        return l
    return -1
