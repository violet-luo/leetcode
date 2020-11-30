"""

Runtime: 40 ms, faster than 9.46% of Python3 online submissions for Rotate Image.
Memory Usage: 14.1 MB, less than 47.44% of Python3 online submissions for Rotate Image.

"""

def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix[0])

    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # reverse each row
    for i in range(n):
        matrix[i].reverse()
