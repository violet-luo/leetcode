"""

Runtime: 28 ms, faster than 69.07% of Python3 online submissions for Summary Ranges.
Memory Usage: 14.3 MB, less than 5.86% of Python3 online submissions for Summary Ranges.

nums = [0,1,2,4,5,7]

"""

def summaryRanges(self, nums: List[int]) -> List[str]:
    res = []

    for i in nums:
        if i-1 not in nums: #[0], [4], [7]
            y = i+1
            while y in nums: #[0,1,2]
                y += 1
            if i == y-1: #[7]
                res.append(str(i))
            else: #[0,1,2], [4,5]
                res.append(str(i) + "->" + str(y-1))
    return res
