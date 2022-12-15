import collections
class Solution:
    def solve(self, board):
        if not board: return 
        n, m = len(board), len(board[0])

        def bfs(x,y):
            queue = collections.deque([(x,y)])
            board[x][y] = '#'
            
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == 'O':
                        board[new_x][new_y] = '#'
                        queue.append((new_x,new_y))
        
        for i in range(n):
            if board[i][0] == 'O':
                bfs(i,0)
            if board[i][m-1] == 'O':
                bfs(i,m-1)
        
        for j in range(m):
            if board[0][j] == 'O':
                bfs(0,j)
            if board[n-1][j] == 'O':
                bfs(n-1,j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

###

def surroundedRegions(board):
    # inner function要在前
    # 将O先设置成D
    def fill(x, y):
        if x < 0 or x > m-1 or y < 0 or y > n-1 or board[x][y] != 'O':
            return
        board[x][y] = 'D'

    def bfs(x, y):
        if board[x][y] == 'O':
            fill(x, y)

        while queue:
            curr = queue.pop(0)
            i, j = curr[0], curr[1]
            fill(i+1, j)
            fill(i-1, j)
            fill(i, j+1)
            fill(i, j-1)

    if len(board) == 0:
        return

    n, m, queue = len(board), len(board[0]), []
    # 遍历第一行和最后一行
    for i in range(m):
        bfs(0, i) # bfs(00, 01, 02, 03)
        bfs(n - 1, i) # bfs(30, 31, 32, 33)

    # 遍历第一列和最后一列
    for j in range(1, n - 1): #跳过第一行和最后一行
        bfs(j, 0) # bfs(10, 20)
        bfs(j, m - 1) # bfs(13, 23)

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'D':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'
