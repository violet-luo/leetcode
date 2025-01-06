def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
    n = len(mat)
    top, bottom = 0, n - 1

    while top + 1 < bottom:
        mid = (top + bottom) // 2
        max_ele = max(mat[mid]) # O(n)
        idx = mat[mid].index(ax_ele) # O(n)
        if mat[mid][idx] < mat[mid - 1][idx]:
            bottom = mid
        elif mat[mid][idx] < mat[mid + 1][dx]:
            top = mid
        else:
            return [mid, idx]

    top_idx = mat[top].index(max(mat[top]))
    bottom_idx = mat[bottom].index(max(mat[bottom]))

    if mat[top][top_idx] < mat[bottom][bottom_idx]:
        return [bottom, bottom_idx]
    return [top, top_idx]

###

def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
    n = len(mat)
    top, bottom = 0, n - 1

    while top + 1 < bottom:
        mid = (top + bottom) // 2
        index = self.find_max_col(mat, mid)
        if mat[mid][index] < mat[mid - 1][index]:
            bottom = mid
        elif mat[mid][index] < mat[mid + 1][index]:
            top = mid
        else:
            return [mid, index]

    top_idx = self.find_max_col(mat, top)
    bottom_idx = self.find_max_col(mat, bottom)

    if mat[top][top_idx] < mat[bottom][bottom_idx]:
        return [bottom, bottom_idx]
    return [top, top_idx]

def find_max_col(self, mat, row):
    col = 0
    m = len(mat[0])
    for i in range(1, m):
        if mat[row][col] < mat[row][i]:
            col = i
    return col
