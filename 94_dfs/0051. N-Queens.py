def solveNQueens(self, n):
    res, subset = [], []
    self.backtrack(n, subset, res)
    return res
  
def backtrack(self, n, subset, res):
    row = len(subset)
    if row == n:
        res.append(self.draw(subset))
        return

    for col in range(n):
        if self.isValid(subset, row, col):
            subset.append(col)
            self.backtrack(n, subset, res)
            subset.pop()

def isValid(self, subset, row, col):
    for r, c in enumerate(subset):
        if c == col: # 有其他皇后在同一列
            return False
        if abs( r - row ) == abs( c - col ): #有其他皇后在同一斜线
            return False
    return True

def draw(self, subset):
    n = len(subset)
    board = []
    for i in range(n):
        row = ['Q' if j == subset[i] else '.' for j in range(n)]
        board.append(''.join(row))
    return board
