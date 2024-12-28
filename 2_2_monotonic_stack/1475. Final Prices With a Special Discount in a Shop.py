def finalPrices(self, prices: List[int]) -> List[int]:
    stack = []  # 存储未比较过的商品索引
    results = list(prices)

    for i in range(len(prices)):
        # 当前价格小于等于之前的价格，更新折扣
        # 如果比前一个小，继续比再前面一个，直到栈为空
        while stack and prices[stack[-1]] >= prices[i]:
            results[stack[-1]] = prices[stack[-1]] - prices[i]
            stack.pop(-1)
        
        stack.append(i) # 当前商品索引入栈
    
    return results
