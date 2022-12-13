def isValidSudoku(self, board: List[List[str]]) -> bool:
    # 先枚举行
    for row in range(9):
        used = set() #换行重置
        for col in range(9):
            if not self.is_valid(board[row][col], used):
                return False
    
    # 再枚举列
    for col in range(9):
        used = set()
        for row in range(9):
            if not self.is_valid(board[row][col], used):
                return False
    
    # 最后枚举方块
    for i in range(3):
        for j in range(3):
            used = set()
            for row in range(i * 3, i * 3 + 3):
                for col in range(j * 3, j * 3 + 3):
                    if not self.is_valid(board[row][col], used):
                        return False
    
    return True

def is_valid(self, c, used):
    if c == '.':
        return True
    if c in used:
        return False
    used.add(c)
    return True
