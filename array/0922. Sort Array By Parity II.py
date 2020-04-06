"""
Runtime: 220 ms, faster than 81.66% of Python3 online submissions for Sort Array By Parity II.
Memory Usage: 15.5 MB, less than 39.13% of Python3 online submissions for Sort Array By Parity II.
"""

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        A_odd = []
        A_even = []
        A_sorted = []
    
        for num in A:
            if num % 2 != 0:
                A_odd.append(num)
            else:
                A_even.append(num)

        for i in range(int(len(A)/2)):
            A_sorted.append(A_even[i])
            A_sorted.append(A_odd[i])

        return A_sorted
