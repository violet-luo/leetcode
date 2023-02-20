def maxProfit(self, prices):
    h1 = h2 = - max(prices) 
    s1 = s2 = 0 
    for price in prices:
        s2,                 h2,                 s1,                 h1 = \
        max(s2, price+h2),  max(h2, -price+s1), max(s1, price+h1),  max(h1, -price) 
    return s2
