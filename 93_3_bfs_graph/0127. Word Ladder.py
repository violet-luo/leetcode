def ladderLength(self, start, end, dict):
    # 假设 dict 不为 null, 首词和尾词是非空的，且二者不相同
    # 首词和尾词可能不在 dict 中，所以必须在 dict 中加入尾词, 可以加入首词
    dict.add(end) 
    queue = collections.deque([start]) 
    visited = set([start])
    distance = 0
    
    # 经典bfs模板
    while queue:
        distance += 1
        for i in range(len(queue)):
            word = queue.popleft()
            if word == end:
                return distance
            for next_word in self.get_next_words(word, dict):
                if next_word in visited:
                    continue
                queue.append(next_word)
                visited.add(next_word)
    return 0

# 找到可以和word接龙的所有单词
# 比如 word = 'hot', dict = {'hot','hit','hog'}, return ['hit','hog']
# 时间复杂度26L^2
def get_next_words(self, word, dict):
    next_words = []
    for i in range(len(word)): #时间复杂度Length #abc
        left, right = word[:i], word[i+1:] #时间复杂度L
        for char in 'abcdefghijklmnopqrstuvwxyz': #遍历下一个可到达的单词
            if word[i] == char:
                continue
            next_words.append(left + char + right) #时间复杂度L #bbc
    return next_words
