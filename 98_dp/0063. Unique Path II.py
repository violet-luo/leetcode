def uniquePathsWithObstacles(self, obstaclesGrid):
    if not obstaclesGrid or not obstacleGrid[0]:
        return 0
    n, m = len(obstacleGrid), len(obstacleGrid[0])

    # 1. state: dp[i][j] 表示从 0,0 走到 i,j 的路径数
    dp = [[0] * m for _ in range(n)]

    # 2. 初始化第0行和第0列
    for i in range(n):
        if obstacleGrid[i][0]:
            break
        dp[i][0] = 1
    for j in range(m):
        if obstacleGrid[0][j]:
            break
        dp[0][j] = 1

    # 3. function
    for i in range(1, n):
        for j in range(1, m):
            if obstacleGrid[i][j]:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]
