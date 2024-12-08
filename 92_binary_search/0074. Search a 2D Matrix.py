def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    n, m = len(matrix), len(matrix[0])
    # 这里不能是l, r = 0, m * n 
    # E.g. matrix = [[1]], target = 1
    # l, r = 0, 0 会直接跳过执行
    l, r = -1, m * n
    
    while l + 1 < r:
        mid = (l + r) // 2
        x, y = mid // m, mid % m
        if matrix[x][y] < target:
            l = mid
        elif matrix[x][y] > target:
            r = mid
        else:
            return True

    return False

###

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
