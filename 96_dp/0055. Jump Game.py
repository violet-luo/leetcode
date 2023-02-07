def canJump(A):
    n = len(A)
    dp = [False] * n # dp[i] 代表能否跳到坐标 i
    dp[0] = True 

    for i in range(1, n):
        for j in range(i): # for 循环上一步
            # 如果存在某点j, dp[j]为true且j可以跳到i, 那么dp[i]为true
            if dp[j] and j + A[j] >= i:
                dp[i] = True
                break

    return dp[n - 1]
