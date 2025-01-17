def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
    n = len(wordsDict)
    i1, i2 = n, n
    min_dist = len(wordsDict)

    for i, word in enumerate(wordsDict):
        if word == word1:
            i1 = i
            if i2 != n:
                min_dist = min(min_dist, abs(i1 - i2))
        if word == word2:
            i2 = i
            if i1 != n:
                min_dist = min(min_dist, abs(i2 - i1))
    
    return min_dist

###

def shortestDistance(wordsDict, word1, word2):
	length = res = len(wordsDict)
	index1 = index2 = length # 不能init成0
	
	for i in range(length):
		if wordsDict[i] == word1:
			index1 = i 
			res = min(res, abs(index1 - index2))
		elif wordsDict[i] == word2:
			index2 = i
			res = min(res, abs(index1 - index2))
	
	return res
