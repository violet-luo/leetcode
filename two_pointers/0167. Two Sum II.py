"""

Runtime: 64 ms, faster than 56.25% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.3 MB, less than 12.20% of Python3 online submissions for Two Sum II - Input array is sorted.

"""
def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return[low + 1, high + 1]
            elif total < target:
                low += 1
            else:
                high -= 1
        return [-1, 1]
