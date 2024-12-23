# 优化
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    n = len(s)

    # base case dp[0]: "" at 0, so n + 1, 前缀型动态规划都是n + 1
    dp = [False] * (n + 1)
    dp[0] = True

    # 优化：找wordDict中最长的单词
    max_length = max([len(word) for word in wordDict])

    for i in range(1, n + 1):
        for l in range(1, max_length + 1):
            # break the loop if l > i, as s[i - l: i] would be invalid
            if i < l:
                break
            # 检查前一个单词是不是True
            # e.g. i - 4, s[:4] = "leet"
            # l = 1, dp[i - l] = dp[3] = False, skip
            # l = 4, dp[i - l] = dp[0] = True, word = s[0:4] = 'leet', dp[4] = True
            if not dp[i - l]:
                continue
            word = s[i - l:i]
            if word in wordDict:
                dp[i] = True
                break
    
    return dp[n]
    
###

def wordBreak(self, s, wordDict):
    n = len(s)
    # base case dp[0]: "", so n + 1, 为了让边界情况也能套用状态转移方程
    # 前缀型动态规划都是n + 1
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break # 可行性，只要找到了，跳出循环

    return dp[n]
