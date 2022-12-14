def totalNQueens(self, n: int) -> int:
    self.count = 0
    subset = []
    self.backtrack(n, subset)
    return self.count

def backtrack(self, n, subset):
    row = len(subset)
    if row == n:
        self.count += 1
        return

    for col in range(n):
        if self.is_valid(subset, row, col):
            subset.append(col)
            self.backtrack(n, subset)
            subset.pop()


def is_valid(self, subset, row, col):
    for r, c in enumerate(subset):
        if c == col: # 有其他皇后在同一列
            return False
        if abs( r - row ) == abs( c - col ): #有其他皇后在同一斜线
            return False
    return True
