def totalNQueens(self, n: int) -> int:
    count = 0
    queen_columns = []

    def dfs(n, queen_columns):
        nonlocal count
        def is_valid(queen_columns, row, col):
            for r, c in enumerate(queen_columns):
                if c == col: # 有其他皇后在同一列
                    return False 
                if abs(r - row) == abs(c - col): #有其他皇后在同一斜线
                    return False
            return True
        
        row = len(queen_columns)
        if row == n: # 递归出口, 所有行都有皇后了
            count += 1
            return
        
        for col in range(n):
            if is_valid(queen_columns, row, col):
                queen_columns.append(col)
                dfs(n, queen_columns)
                # 找到第一个solution之后backtrack到上一个valid column找其他的solution
                queen_columns.pop() 
    dfs(n, queen_columns)
    return count
    
###

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
