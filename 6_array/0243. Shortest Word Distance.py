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
