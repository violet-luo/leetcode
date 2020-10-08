"""

Runtime: 32 ms, faster than 91.14% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.1 MB, less than 16.80% of Python3 online submissions for Merge Sorted Array.

"""

import re
    
def myAtoi(self, s: str) -> int:
    maxii = 2147483647                         # define the maximum limit
    minii = -2147483648                        # define minimum limit
    s = s.strip()                              # Remove all whitespaces
    if not s:
        return 0
    sign, idx = 1, 0                                  # sign set to 1 -> Positive, index set to 0
    if s[idx]=='+':                                   # check if the first character is a '+'
        idx+=1                                        # if so, move index to next character
    elif s[idx]=='-':                                 # check if first character is '-'
        sign = -1                                     # change status of sign to be a negative number
        idx+=1                                        # update the index
    num = 0
    n = len(s)
    while idx<n:
        if not s[idx].isdigit():            # if the number is not a digit, then stop
            break
        num = num*10 + ord(s[idx])-ord('0') # else move the units, tenths, hundredth... places by multiplying the number by 10 and add the unicode integer
        if num>maxii:
            break
        idx+=1
    return min(max(sign*num, minii), maxii) # return answer if its within the maximum and minimum range
