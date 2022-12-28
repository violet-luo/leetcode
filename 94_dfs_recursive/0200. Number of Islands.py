def numIslands(grid):
    n, m = len(grid), len(grid[0])
    visited = set()
    count = 0

    def dfs(x, y):
        grid[x][y] = 0
        visited.add((x, y))

        for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            x_, y_ = x + dx, y + dy
            if 0 <= x_ < n and 0 <= y_ < m and (x_, y_) not in visited and grid[x_][y_] == '1':
                dfs(x_, y_)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1': # 这里不一样
                dfs(i, j)
                count += 1

    return count
