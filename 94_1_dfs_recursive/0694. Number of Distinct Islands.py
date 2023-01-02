def numberofDistinctIslands(self, grid):
    n, m = len(grid), len(grid[0])
    visited = set()

    def dfs(x, y, cur_island, bx, by):
        grid[x][y] = 0
        cur_island.add((x - bx, y - by))
        for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != 1:
                continue
            dfs(nx, ny, cur_island, bx, by)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                cur_island = set()
                dfs(i, j, cur_island, i, j)
                visited.add(tuple(cur_island))
    
    return len(visited)
