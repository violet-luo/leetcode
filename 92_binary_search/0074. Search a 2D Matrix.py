def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    n, m = len(matrix), len(matrix[0])

    l, r = 0, n * m - 1
    while l <= r:
        mid = (l + r) // 2
        element = matrix[mid // m][mid % m]
        if target == element:
            return True
        elif target < element:
            r = mid - 1
        else:
            l = mid + 1

    return False
