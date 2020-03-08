# Beats 82%

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
