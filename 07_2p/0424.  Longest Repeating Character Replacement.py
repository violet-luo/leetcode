def characterReplacement(self, s, k):
    if not s:
        return 0

    # j指向满足条件的子字符串的后面一个位置
    j = 0
    maxFreq = 0
    counter = {}
    answer = 0
    for i in range(len(s)): #O(n)
        # 找到i ~ j-1这一段是最长的以i开头，满足不超过k次替换的子字符
        while j < len(s) and j - i - maxFreq <= k: #O(n)
            counter[s[j]] = counter.get(s[j], 0) + 1
            maxFreq = max(maxFreq, counter[s[j]])
            j += 1

        if j - i - maxFreq > k:
            # i ~ j-1 的 substring 需要 k+1
            # i ~ j-2 的 substring 只需要 k
            answer = max(answer, j - i - 1)
        else:
            # i ~ j-1 的 substring <= k 替换
            answer = max(answer, j - i)

        counter[s[i]] -= 1
        maxFreq = max(counter.values())

    return answer
