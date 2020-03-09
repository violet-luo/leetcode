"""
Recursion

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



"""
Runtime: 28 ms, faster than 79.18% of Python3 online submissions for Plus One.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Plus One.
"""

def plusOne(List):
    if List[-1] != 9:
        List[-1] = List[-1] + 1
    elif set(List) == {9}: 
        List = [1] + [0] * len(List)
    else: 
        #find the index of the last non-nine digit
        i = len(List) - 1 - next((i for i, x in enumerate(reversed(List)) if x != 9), None)
        List[:i], List[i], List[i+1:] = List[:i], List[i] + 1, [0] * (len(List) - 1 - i)
    return List
