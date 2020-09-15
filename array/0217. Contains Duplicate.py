"""

Runtime: 132 ms, faster than 55.05% of Python3 online submissions for Contains Duplicate.
Memory Usage: 19.2 MB, less than 55.42% of Python3 online submissions for Contains Duplicate.

"""

def containsDuplicate(self, nums: List[int]) -> bool:
    res = set()

    for num in nums:
        if num in res:
            return True
        res.add(num)
    return False
