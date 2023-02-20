def maxProfit(self, prices):
    n = len(prices)
    dp = [[0] * 2 for _ in range(n)] # 不能是[0][0]

    dp[0][0] = 0
    dp[0][1] = - prices[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]) # 前一天持有，今天卖出
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]) # 前一天不持有，今天买入

    return dp[n-1][0]    # 返回最后一天且手上没有股票时的获利情况
