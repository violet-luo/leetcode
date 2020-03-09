"""
Runtime: 32 ms, faster than 48.52% of Python3 online submissions for Plus One.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Plus One.
"""

def plusOne(self, List):
    if List[-1] != 9:
        List[-1] = List[-1] + 1
    elif set(List) == {9}: 
        List = [1] + [0] * len(List)
    else: 
        List[-1], List[:-1] = 0, self.plusOne(List[:-1])
    return List
