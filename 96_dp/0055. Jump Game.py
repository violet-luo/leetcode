def canJump(A):
    if not A:
        return False

    n = len(A)
    # 1. state: dp[i] 代表能否跳到坐标 i
    dp = [False] * n 

    # 2. 初始化：一开始站在0
    dp[0] = True 

    # 3. function
    for i in range(1, n):
        for j in range(i): # for 循环上一步
            # 高效的写法
            if dp[j] and j + A[j] >= i: #上一步j是True && j + j的步数大于等于到i的距离
                dp[i] = True
                break
            # 偷懒的写法
            dp[i] = dp[i] or dp[j] and (j + A[j] >= i)

    # 4. answer
    return dp[n - 1]
