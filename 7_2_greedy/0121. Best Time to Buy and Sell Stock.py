def maxProfit(self, prices):
    # find the max profit = max(prices[j] - prices[i]) , j >= i，可以同日交易
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
