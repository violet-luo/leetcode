# 自顶向下
def shortestPath2(grid):
    if not grid or not grid[0]:
        return -1
    n, m = len(grid), len(grid[0])

    # 1. state: f[i][j] 代表从 0,0 跳到 i,j 的最少步数
    dp = [[float('inf')] * m for _ in range(n)]

    # 2. 初始化f[0][0]是起点
    dp[0][0] = 0

    # 3. function
    for j in range(m):
        for i in range(n):
            if grid[i][j]:
                continue
            for dx, dy in [(-1, -2), (1, -2), (-2, -1), (2, -1)]: #因为自顶向下，所以方向反过来
                x, y = i + dx, i + dy
                if 0 <= x < n and 0 <= y < m:
                    dp[i][j] = min(dp[i][j], dp[x][y] + 1)

    # 4. answer
    if dp[n - 1][(m - 1)] == float('inf'):
        return -1
    return dp[n - 1][(m - 1)]
