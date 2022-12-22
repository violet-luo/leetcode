### 1.
def backPack(self, m, A):
    n = len(A)
    # state: dp[i][j] 代表前 i 个数里能否挑出若干个数组成 j 的和
    # 注意这是一个 (n+1) * (m+1) 的二维数组而不是 n*m 的二维数组
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    # initiazlize: 前0个数能凑出0的和，其他的非0和都凑不出来
    dp[0][0] = True
    
    # function
    for i in range(1, n+1):
        dp[i][0] = True
        for j in range(1, m+1):
            if j >= A[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-A[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    
    # answer
    for i in range(m, -1, -1):
        if dp[n][i]:
            return i
    return -1
  
  ### 2.
  def backPack(self, m, A):
    n = len(A)
    # state: dp[i][j] 代表前 i 个数里能否挑出 <= j 的最大和
    # 注意这是一个 (n+1) * (m+1) 的二维数组而不是 n*m 的二维数组
    dp = [[0] * (m+1) for _ in range(n + 1)]
    
    # function
    for i in range(1, n+1):
        for j in range(0, m+1):
            if j >= A[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]] + A[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    # answer
    return dp[n][m]
