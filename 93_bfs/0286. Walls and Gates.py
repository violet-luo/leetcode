288. Walls and Gates

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
