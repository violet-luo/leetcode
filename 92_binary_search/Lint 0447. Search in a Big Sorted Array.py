def searchBigSortedArray(nums, target):
    # 初始化查找范围为1，代表前1个数中查找
    range_total = 1
    # 倍增法：如果target在查找范围之外，查找范围翻倍，时间复杂度O(logK)
    while nums.get(range_total - 1) < target:
        range_total = range_total * 2
    
    # 二分模板
    # l 也可以是 range_total // 2。但是写0也不会影响时间复杂度
    # 如果target前rangeTotal中，则index范围为[0, rangeTotal - 1]
    # O(logK)
    l, r = 0, range_total - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums.get(mid) < target:
            l = mid
        # 要点：为什么这里target == mid, 不直接返回？
        # 因为在中点左边还可能存在更靠左的target
        else:
            r = mid

    if nums.get(l) == target:
        return l
    if nums.get(r) == target:
        return r
    return -1
