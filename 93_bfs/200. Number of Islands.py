from collections import deque

DIRECTIONS = [(1, 0), #右
              (0, -1), #上
              (-1, 0), #左
              (0, 1) #下
              ]

def numIslands(grid):
    if not grid or not grid[0]:
        return 0

    islands = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in visited:
                bfs(grid, i, j, visited)
                islands += 1

    return islands                    

def bfs(grid, x, y, visited):
    queue = deque([(x, y)])
    visited.add((x, y))
    while queue:
        x, y = queue.popleft()
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if is_invalid(grid, next_x, next_y, visited):
                continue
            queue.append((next_x, next_y))
            visited.add((next_x, next_y))

def is_invalid(grid, x, y, visited):
    n, m = len(grid), len(grid[0])
    # 越界
    if x < 0 or x >= n or y < 0 or y >= m:
        return True
    # 岛屿已经访问过
    if (x, y) in visited:
        return True
    # 不是岛屿
    if grid[x][y] == 0:
        return True
    return False
