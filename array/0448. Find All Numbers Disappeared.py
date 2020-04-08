"""
Credit to @leetcodeftw

Explanation: All the numbers are positive. Once we visit a number, we make it negative and return positive numbers we have not visitied at the end.

"""

def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])
            
    return [i + 1 for i, num in enumerate(nums) if num > 0]
