def maxProfit(self, prices):
    n = len(prices)
    dp = [0] * n
    min_price = prices[0] 

    for i in range(1, n):
        min_price = min(min_price, prices[i])
        dp[i] = max(dp[i - 1], prices[i] - min_price)

    return dp[n-1]
