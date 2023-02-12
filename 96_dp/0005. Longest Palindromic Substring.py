def longestPalindrome(self, s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    max_len, start = 1, 0 # 初始长度为1，如果不存在回文，就返回1

    for j in range(1, n):
        for i in range(j): # 不能是 (1, j)
            # 初始化：头尾相等（s[i]==s[j]）就能返回True
            if j - i <= 2 and s[i] == s[j]:
                dp[i][j] = True
                cur_len = j - i + 1
            # 去掉头尾之后还是一个回文且头尾相等
            elif dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                cur_len = j - i + 1
            # 出现回文更新输出
            if dp[i][j] and cur_len > max_len:
                max_len = cur_len
                start = i

    return s[start:start + max_len]
