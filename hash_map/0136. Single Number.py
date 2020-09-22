"""

1. Time Complexity: O(N), Space Complexity: O(1) - Bit Manipulation

Runtime: 116 ms, faster than 33.87% of Python3 online submissions for Single Number.
Memory Usage: 16.3 MB, less than 66.95% of Python3 online submissions for Single Number.

"""
def singleNumber(self, nums: List[int]) -> int:
    a = 0
    for i in nums:
        a ^= i
    return a
    
    
"""

2. Time Complexity: O(N), Space Complexity: O(N) - List
Runtime: 1784 ms, faster than 10.78% of Python3 online submissions for Single Number.
Memory Usage: 16.5 MB, less than 5.26% of Python3 online submissions for Single Number.

"""
def singleNumber(self, nums: List[int]) -> int:
    no_dupe = []

    for num in nums:
        if num not in no_dupe:
            no_dupe.append(num)
        else:
            no_dupe.remove(num)
    return no_dupe.pop()
   
   
"""

3. Time Complexity: O(N), Space Complexity: O(N) - Hash

Runtime: 96 ms, faster than 46.64% of Python3 online submissions for Single Number.
Memory Usage: 16.4 MB, less than 24.11% of Python3 online submissions for Single Number.

"""
def singleNumber(self, nums: List[int]) -> int:
    no_dupe = {}

    for num in nums:
        if num not in no_dupe:
            no_dupe[num] = 1
        else:
            no_dupe[num] += 1

    # items() method is used to return the list with all dictionary keys with values
    for key,val in no_dupe.items():
        if val == 1:
            return key
   
   
"""

4. Time Complexity: O(N), Space Complexity: O(N) - Math

Runtime: 80 ms, faster than 96.10% of Python3 online submissions for Single Number.
Memory Usage: 16.2 MB, less than 86.90% of Python3 online submissions for Single Number.

"""

def singleNumber(self, nums: List[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)
