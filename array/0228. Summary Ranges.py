"""

Runtime: 28 ms, faster than 69.07% of Python3 online submissions for Summary Ranges.
Memory Usage: 14.3 MB, less than 5.86% of Python3 online submissions for Summary Ranges.

"""

def summaryRanges(self, nums: List[int]) -> List[str]:
    res = []

    for i in nums:
        if i-1 not in nums:
            y = i+1
            while y in nums:
                y += 1
            if i == y-1:
                res.append(str(i))
            else:
                res.append(str(i) + "->" + str(y-1))
    return res
