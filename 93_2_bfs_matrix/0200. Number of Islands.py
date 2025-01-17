def numIslands(self, grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    n, m = len(grid), len(grid[0])
    islands = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                q = collections.deque([(i, j)])
                grid[i][j] = '0'
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == '1':
                            grid[new_x][new_y] = '0'
                            q.append((new_x, new_y))
                
                islands += 1
    
    return islands
    
###

def numIslands(grid):
    if not grid or not grid[0]: return 0
    n, m = len(grid), len(grid[0])

    def bfs(x, y):
        queue = deque([(x, y)])
        grid[x][y] = '0'
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == '1':
                    queue.append((new_x, new_y))
                    grid[new_x][new_y] = '0'

    islands = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                bfs(i, j)
                islands += 1

    return islands

###

def numIslands(self,grid):
    if not grid or not grid[0]: #grid是[[]]
        return 0

    islands = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in visited:
                self.bfs(grid, i, j, visited)
                islands += 1

    return islands                    

# 标准宽搜遍历一个岛
def bfs(self, grid, x, y, visited):
    queue = collections.deque([(x, y)])
    visited.add((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]: #右左下上
            next_x = x + dx
            next_y = y + dy
            if self.is_invalid(grid, next_x, next_y, visited):
                continue
            queue.append((next_x, next_y))
            visited.add((next_x, next_y))

def is_invalid(self, grid, x, y, visited):
    n, m = len(grid), len(grid[0])
    # 1. 越界
    if x < 0 or x >= n or y < 0 or y >= m:
        return True
    # 2. 岛屿已经访问过
    if (x, y) in visited:
        return True
    # 3. 不是岛屿
    if grid[x][y] == 0:
        return True
    return False
