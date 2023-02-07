def jump(self, nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            # 如果从j可以跳到i
            if nums[j] + j >= i:
                dp[i] = min(dp[i], dp[j] + 1) #dp[j]是从下标[0,i)中能够走到位置i的所有情况
                break
    return dp[n - 1]
