def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
    n = len(wordsDict)
    i1, i2 = n, n
    min_dist = n

    for i, word in enumerate(wordsDict):
        if word == word1:
            i1 = i
            if i2 != n and i1 != i2: # 与243区别 # i2要被更新过
                min_dist = min(min_dist, abs(i1 - i2))
        if word == word2:
            i2 = i
            if i1 != n and i1 != i2:  # 与243区别
                min_dist = min(min_dist, abs(i2 - i1))
    return min_dist
