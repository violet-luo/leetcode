"""

Runtime: 100 ms, faster than 32.18% of Python3 online submissions for Two Sum.
Memory Usage: 15.3 MB, less than 31.49% of Python3 online submissions for Two Sum.

https://leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time

"""

def twoSum(self, numbers, target):
    d = {}
    for i, n in enumerate(numbers):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i
