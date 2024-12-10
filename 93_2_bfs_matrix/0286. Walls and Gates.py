def wallsAndGates(self, rooms: List[List[int]]) -> None:
    if not rooms or not rooms[0]:
        return 0

    n, m = len(rooms), len(rooms[0])
    for i in range(n):
        for j in range(m):
            if rooms[i][j] == 0:
                q = collections.deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        next_x, next_y = x + dx, y + dy
                        # 如果neighbor现有的value比移动x, y + 1大，overwrite
                        if 0 <= next_x < n and 0 <= next_y < m and rooms[next_x][next_y] != -1:
                            if rooms[next_x][next_y] > rooms[x][y] + 1:
                                q.append((next_x, next_y))
                                rooms[next_x][next_y] = rooms[x][y] + 1
                                
###

def wallsAndGates(rooms):
    if not rooms or not rooms[0]: return rooms
    n, m = len(rooms), len(rooms[0])

    def bfs(x, y):
        queue = collections.deque([(x,y)])

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = x+dx, y+dy
                if is_invalid(next_x, next_y):
                    continue
                if rooms[next_x][next_y] > rooms[x][y] + 1:
                    queue.append((next_x, next_y))
                    rooms[next_x][next_y] = rooms[x][y] + 1

    def is_invalid(x, y):
        if x >= n or x < 0: return True 
        if y >= m or y < 0: return True
        if rooms[x][y] == -1: return True
        return False

    for i in range(n):
        for j in range(m):
            if rooms[i][j] == 0:
                bfs(i, j)
                
    return rooms

###

def wallsAndGates(self, grid):
    if not grid or not grid[0]:
        return grid
    
    queue = collections.deque([])
    visited = set()
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                # 先找门，这题和number of islands不同处是不在这里做BFS
                queue.append((i, j))
                visited.add((i, j))
   
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]: #右左下上
            next_x, next_y = x + dx, y + dy
            if self.is_invalid(grid, next_x, next_y, visited):
                continue
            queue.append((next_x, next_y))
            visited.add((next_x, next_y))
            grid[next_x][next_y] = grid[x][y] + 1
    return grid
            
                
def is_invalid(self, grid, x, y, visited):
    n, m = len(grid), len(grid[0])
    if x < 0 or x >= n or y < 0 or y >= m:
        return True
    if (x, y) in visited:
        return True
    if grid[x][y] != 2147483647:
        return True
    return False
