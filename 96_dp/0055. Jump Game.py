def canJump(self, nums: List[int]) -> bool:
    n = len(nums)

    # state: dp[i] 代表能否跳到坐标 i
    dp = [False] * n

    # initialization: 一开始站在0这个位置
    dp[0] = True

    # function
    # loop thru each index from 1 to n - 1 to see if it's reachable
    for i in range(1, n):
        # for each index, loos thru all previous indices j from 0 to i - 1
        for j in range(i):
            # 高效的写法
            # dp[j]: can we reach index j?
            # j + nums[j] >= i: from index j, can we reach i?
            if dp[j] and j + nums[j] >= i:
                dp[i] = True
                break
            
            # 偷懒的写法
            dp[i] = dp[i] or dp[j] and (j + nums[j] >= i)
    
    return dp[n - 1]
