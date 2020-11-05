"""

Runtime: 40 ms, faster than 83.55% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.4 MB, less than 24.85% of Python3 online submissions for Search a 2D Matrix.

"""

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])

    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        element = matrix[mid // n ][mid % n]
        if target == element:
            return True
        elif target < element:
            right = mid - 1
        else:
            left = mid + 1

    return False
