def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
        
    n, m = len(matrix), len(matrix[0])
    start, end = 0, n * m - 1
    while start + 1 < end:
        mid = (start + end) // 2
        x, y = mid // m, mid % m
        if matrix[x][y] < target:
            start = mid
        elif matrix[x][y] > target:
            end = mid
        else:
            return True
            
    x, y = start // m, start % m
    if matrix[x][y] == target:
        return True
    
    x, y = end // m, end % m
    if matrix[x][y] == target:
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
