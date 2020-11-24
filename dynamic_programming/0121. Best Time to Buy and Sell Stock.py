"""

Runtime: 60 ms, faster than 69.79% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 15.1 MB, less than 9.72% of Python3 online submissions for Best Time to Buy and Sell Stock.

"""

def maxProfit(self, prices: List[int]) -> int:
    profit, min_buy = 0, float('inf')
    for price in prices:
        min_buy = min(min_buy, price)
        profit = max(profit, price - min_buy)
    return profit
