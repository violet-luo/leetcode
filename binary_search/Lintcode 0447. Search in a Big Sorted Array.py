def searchBigSortedArray(self, reader, target):
    # 初始化查找范围为1，代表前1个数中查找
    range_total = 1
    # 倍增法：如果target在查找范围之外，查找范围翻倍，时间复杂度O(logK)
    while reader.get(range_total - 1) < target:
        range_total = range_total * 2

    # 经典二分法
    # start 也可以是 range_total // 2
    # 但是写0也不会影响时间复杂度
    # 如果target前rangeTotal中，则index范围为[0, rangeTotal - 1]
    # 时间复杂度O(logK)
    start, end = 0, range_total - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        # 如果 mid < target, target在右边，丢弃左边
        if reader.get(mid) < target:
            start = mid
        # 要点：为什么这里target == mid, 不直接返回？
        # 因为在中点左边还可能存在更靠左的target
        else:
            end = mid

    # 要点：为什么这里先检查start, 再检查end?
    # 因为我们要求的是first index, 所以先检查更靠左的start
    # 如果start不为target, 再检查稍微靠右的end
    if reader.get(start) == target:
        return start
    if reader.get(end) == target:
        return end
    return -1
