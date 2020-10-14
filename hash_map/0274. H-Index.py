"""

Runtime: 32 ms, faster than 90.01% of Python3 online submissions for H-Index.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for H-Index.

"""
def hIndex(self, citations):
    citations.sort()
    n = len(citations)
    for i in xrange(n):
        if citations[i] >= (n-i):
            return n-i
    return 0
