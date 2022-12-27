def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return 0

    n, m = len(matrix), len(matrix[0])
    for row in matrix:
        if row[0] <= target <= row[-1]:
            l, r = 0, m - 1
            while l + 1 < r:
                mid = (l + r) // 2
                if row[mid] < target:
                    l = mid
                elif row[mid] > target:
                    r = mid
                else:
                    return True
            if row[l] == target or row[r] == target:
                return True
    return False

###

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return 0

    n, m = len(matrix), len(matrix[0])
    for row in matrix:
        # locate the row
        if row[0] <= target <= row[-1]:
            l, r = 0, m - 1
            while l <= r:
                mid = (l + r) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
    return False

###

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
        
    n, m = len(matrix), len(matrix[0])
    # 从左下出发
    i, j = n - 1, 0
    while i >= 0 and j < m:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            j += 1
        elif matrix[i][j] > target:
            i -= 1
    return False
