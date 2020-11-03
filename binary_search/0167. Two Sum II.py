"""

Runtime: 100 ms, faster than 12.47% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.4 MB, less than 10.94% of Python3 online submissions for Two Sum II - Input array is sorted.

"""

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i in range(n):
        start, end = i + 1, n - 1
        while start <= end:
            mid = (start + end) // 2
            if numbers[mid] == target - numbers[i]:
                return [i + 1, mid + 1]
            elif numbers[mid] > target - numbers[i]:
                end = mid - 1
            else:
                start = mid + 1

    return [-1, -1]
