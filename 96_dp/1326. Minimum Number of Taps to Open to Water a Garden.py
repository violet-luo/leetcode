def minTaps(n: int, ranges: list[int]) -> int:
    # dp[i]: minimum number of taps needed to water the garden up to position i
    # 1. initialize
    dp = [math.inf] * (n + 1)  # 设定所有位置初始为不可达（无穷大）
    dp[0] = 0  # 位置 0 处不需要打开水龙头

    # 2. 遍历每个水龙头，更新 DP 数组
    for i in range(n + 1):
        # 计算它的覆盖范围，left不小于0，right不超过n
        left, right = max(0, i - ranges[i]), min(n, i + ranges[i])
        
        for j in range(left, right + 1):  # 遍历该水龙头覆盖的范围
            dp[j] = min(dp[j], dp[left] + 1)  # 选最少的水龙头数量

    return dp[n] if dp[n] != math.inf else -1
