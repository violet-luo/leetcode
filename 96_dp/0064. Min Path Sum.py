def minPathSum(self, grid):
    m, n = len(grid), len(grid[0])
    dp = [[0 for j in range(0, n)] for i in range(0, m)]

    # 2. 初始化第0行和第0列
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # 状态转移
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    # 返回结果
    return dp[m - 1][n - 1]
