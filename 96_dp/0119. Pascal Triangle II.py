def getRow(self, rowIndex):
    dp = [1] * (rowIndex + 1)
    for i in range(1, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            dp[j] += dp[j - 1]
    return dp
