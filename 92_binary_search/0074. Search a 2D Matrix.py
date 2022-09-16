def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
        
    n, m = len(matrix), len(matrix[0])
    l, r = 0, n * m - 1
    while l <= r:
        mid = (l + r) // 2
        element = matrix[mid // m][mid % m]
        if element == target:
            return True
        elif element < target:
            l = mid + 1
        else:
            r = mid - 1

    return False
