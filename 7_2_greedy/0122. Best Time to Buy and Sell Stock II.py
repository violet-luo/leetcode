def maxProfit(self, prices):
    profit = 0

    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            profit += prices[i + 1] - prices[i]

    return profit
    
###

def maxProfit(self, prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] - prices[i - 1] > 0:
            profit += prices[i] - prices[i - 1]
    return profit
