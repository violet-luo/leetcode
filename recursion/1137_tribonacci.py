"""

https://leetcode.com/problems/n-th-tribonacci-number/

Given n, return the value of Tn.
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2: 
            return 1
        else:
            return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            
