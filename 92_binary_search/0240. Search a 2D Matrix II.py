"""

Runtime: 40 ms, faster than 43.17% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 18.8 MB, less than 83.76% of Python3 online submissions for Search a 2D Matrix II.

"""

def searchMatrix(self, matrix, target):
    if len(matrix) == 0:
        return False

    y = len(matrix) - 1
    x_range = len(matrix[0]) - 1
    x = 0

    while x <= x_range and y >= 0:
        if target > matrix[y][x]:
            x += 1
        elif target < matrix[y][x]:
            y -= 1
        else:
            return True

    return  False
