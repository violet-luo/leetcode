def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix[0])

    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # reverse each row
    for i in range(n):
        matrix[i].reverse()
