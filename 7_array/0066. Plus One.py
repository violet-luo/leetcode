"""
Three Scenarios
1. 24+1=25
2. 29+1=30
3. 99+1=100
"""

1. 
def plusOne(digits: List[int]): #[1,2,9], [9,9]
    for i in range(len(digits)-1, -1, -1):
        if digits[i] != 9: # [1,3,0]
            digits[i] += 1
            return digits
        else:
            digits[i] = 0 # [1,2,0], [9, 0], [0,0]
            if digits[0] == 0:
                digits.insert(0,1) # [1,0,0]
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
