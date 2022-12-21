## 自底向上
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

def minimumTotal(self, triangle):
    n = len(triangle)

    # state: dp[i][j] 代表从 i,j 走到最底层的最短路径值
    # 0 [0]
    # 1 [0] [0]
    # 2 [0] [0] [0]
    # 3 [0] [0] [0]
    dp = [[0] * (i + 1) for i in range(n)]

    # initialize: 初始化终点（最后一层）
    # 3 [4] [1] [8] [3]
    for i in range(n):
        dp[n-1][i] = triangle[n-1][i]

    # function: 从下往上倒过来推导，计算每个坐标到哪儿去
    # 0 [11]
    # 1 [9] [10]
    # 2 [7] [6] [10]
    # 3 [4] [1] [8] [3]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

    # answer: 起点就是答案
    return dp[0][0]
  
## 自顶向下
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

def minimumTotal(self, triangle):
    n = len(triangle)
    
    # state: dp[i][j] 代表从 0, 0 走到 i, j 的最短路径值
    dp = [[0] * (i + 1) for i in range(n)]
    
    # initialize: 三角形的左边和右边要初始化，因为他们分别没有左上角和右上角的点
    # 0 [2]
    # 1 [5] [6]
    # 2 [11] [0] [13]
    # 3 [15] [0] [0] [16]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + triangle[i][0]
        dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
    
    # function: dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    # i, j 这个位置是从位置 i - 1, j 或者 i - 1, j - 1 走过来的
    # 0 [2]
    # 1 [5] [6]
    # 2 [11] [10] [13]
    # 3 [15] [11] [18] [16]
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
           
    # answer: 最后一层的任意位置都可以是路径的终点
    return min(dp[n - 1])
