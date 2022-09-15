def firstBadVersion(self, n):
    l, r = 1, n # 题目定义从1开始
    
    while l < r:
        mid = (l + r) // 2
        if isBadVersion(mid):
            r = mid
        else:
            l = mid + 1 # mid 查过了，从mid后面一个数开始查
    return r
