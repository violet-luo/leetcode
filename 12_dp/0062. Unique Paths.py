// 1. 自顶向下
def uniquePaths(self, m, n):
    # state: dp[i][j] 代表从0,0走到i,j的方案总数
    dp = [[0] * n for _ in range(m)]

    # initialize: 初始化第0行和第0列
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # function: dp[i][j] = dp[i-1][j] + dp[i][j-1]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # answer
    return dp[m-1][n-1]

// 2. 自底向上
def uniquePaths(self, m, n):
    # state: dp[i][j] 代表从i,j走到m-1, n-1的方案总数
    dp = [[0] * n for _ in range(m)]

    # initialize: 初始化第m-1行和第n-1列
    for i in range(m):
        dp[i][n-1] = 1
    for j in range(n):
        dp[m-1][j] = 1

    # function: dp[i][j] = dp[i+1][j] + dp[i][j+1]
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1):
            dp[i][j] = dp[i+1][j] + dp[i][j+1]

    # answer
    return dp[0][0]
