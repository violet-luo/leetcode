def firstBadVersion(n):
    start, end = 1, n # 题目定义从1开始
    
    while start + 1 < end:
        mid = (start + end) // 2
        if isBadVersion(mid): # 相当于first position == target
            end = mid
        else:
            start = mid

    if isBadVersion(start):
        return start
    return end
