def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
    # Sort rides by their ending position
    # So DP can calculate the max profit reaching each location
    rides.sort(key=lambda x: x[1]) 
    
    # dp[i] 第 i 个行程时，最多可以获得的收益
    dp = [0] * (len(rides) + 1)
    end_positions = [ride[1] for ride in rides]

    for i in range(len(rides)):
        start, end, tip = rides[i]
        earning = end - start + tip
        
        # 二分查找，找到最后一个不与当前行程重叠的行程索引
        # 即第一个结束时间大于等于 start 的索引
        idx = bisect_right(end_positions, start) - 1
        
        # dp[i] 不选当前行程
        # 选当前行程：上一个不重叠行程的最大收益 + 当前行程的收益
        dp[i + 1] = max(dp[i], (dp[idx + 1] if idx >= 0 else 0) + earning)
    
    return dp[-1]
