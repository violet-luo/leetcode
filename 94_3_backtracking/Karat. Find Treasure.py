def find_treasure(board, start, end):
    n, m = len(board), len(board[0])
    treasure = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                treasure += 1
    paths = []
    visited = set()
    
    def dfs(x, y, path, treasure_left):
        if x >= n or x < 0 or y >= m or y < 0: return
        if board[x][y] == -1: return
        if (x,y) in visited: return
        
        path.append((x,y))
        temp = board[x][y]
        print(x, y, temp)
        if temp == 1:
            treasure_left -= 1
        visited.add((x,y))
            
        if x == end[0] and y == end[1] and treasure_left == 0:
            paths.append(path[:])
            path.pop()
            board[x][y] = temp
            return
        
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            dfs(x+dx, y+dy, path, treasure_left)

        board[x][y] = temp
        path.pop()
        
    dfs(start[0], start[1], [], treasure)
    
    min_len = float('inf')
    min_len_path = []
    for path in paths:
        if len(path) < min_len:
            min_len = len(path)
            min_len_path = path
    return min_len_path
