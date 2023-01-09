def plusOne(self, digits):
    for i in range(len(digits)-1, -1, -1):
        digits[i] += 1 #持续进1
        if digits[i] == 10:
            digits[i] = 0
        else:
            break
    if digits[0] == 0:
        digits.insert(0, 1)
    return digits


"""
2. Recursion

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
