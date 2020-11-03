"""

Runtime: 24 ms, faster than 90.13% of Python3 online submissions for First Bad Version.
Memory Usage: 14.2 MB, less than 99.99% of Python3 online submissions for First Bad Version.

"""

def firstBadVersion(self, n):
    start, end = 1, n 

    while start < end:
        mid = start + (end - start) // 2 # to avoid overflow
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1
    return end
