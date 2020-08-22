"""

Runtime: 48 ms, faster than 18.56% of Python3 online submissions for Rotate String.
Memory Usage: 13.6 MB, less than 98.41% of Python3 online submissions for Rotate String.

"""

def rotateString(self, A: str, B: str) -> bool:
    if A == B:
        return True

    if len(A) == len(B):
        for i in range(len(A)):
            if A == B[i:] + B[:i]:
                return True
    return False
    
    
    
"""

Solution

Runtime: 44 ms, faster than 24.70% of Python3 online submissions for Rotate String.
Memory Usage: 13.8 MB, less than 62.94% of Python3 online submissions for Rotate String.

"""

def rotateString(self, A, B):
        return len(A) == len(B) and B in A+A
