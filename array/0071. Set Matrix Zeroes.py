"""

1. Extra space
Runtime: 124 ms, faster than 85.38% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 15 MB, less than 66.39% of Python3 online submissions for Set Matrix Zeroes.

"""

def setZeroes(self, matrix: List[List[int]]) -> None:
    R = len(matrix)
    C = len(matrix[0])
    rows, cols = set(), set()

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0
         
         
"""

2. No extra space
Runtime: 124 ms, faster than 85.38% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 15 MB, less than 66.39% of Python3 online submissions for Set Matrix Zeroes.

"""

def setZeroes(self, matrix: List[List[int]]) -> None:
    is_col = False
    R = len(matrix)
    C = len(matrix[0])

    for i in range(R):
        if matrix[i][0] == 0:
            is_col = True
        for j in range(1, C):
            # If an element is zero, we set the first element of the corresponding row and column to 0
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, R):
        for j in range(1, C):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

    # See if the first row needs to be set to zero as well
    if matrix[0][0] == 0:
        for j in range(C):
            matrix[0][j] = 0

    # See if the first column needs to be set to zero as well  
    if is_col:
        for i in range(R):
            matrix[i][0] = 0
