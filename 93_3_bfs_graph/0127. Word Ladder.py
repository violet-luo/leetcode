def ladderLength(self, start, end, dict):
    # 假设 dict 不为 null, beginWord 和 endWord 是非空的，且二者不相同
    # 起始单词和结束单词可能不在 dict 中，所以必须在 dict 中加入 end, 可以加入start
    dict.add(end) 
    queue = collections.deque([start]) 
    visited = set([start])
    
    distance = 0
    # 经典bfs模板
    while queue:
        # 到当前层的长度
        distance += 1
        # 当前层有size个元素
        size = len(queue)
        for i in range(size):
            word = queue.popleft()
            # 如果当前层的词为尾词，直接返回当前的长度
            if word == end:
                return distance

            # 如果不是终点，for循环它的邻居结点
            for next_word in self.get_next_words(word, dict):
                if next_word in visited:
                    continue
                queue.append(next_word)
                visited.add(next_word)
    return 0

# 找到可以和word接龙的所有单词
# 比如word = 'hot', dict = {'hot','hit','hog'}, return ['hit','hog']
# 时间复杂度26L^2
def get_next_words(self, word, dict):
    next_words = []
    for i in range(len(word)): #时间复杂度Length #abc
        left, right = word[:i], word[i+1:] #时间复杂度L
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if word[i] == char:
                continue
            # 在s中，把位置index的字母替换成c，返回替换后的字符串
            next_word = left + char + right #时间复杂度L #bbc
            # 如果字母替换后的单词存在于dict, 加入next_words
            if next_word in dict: #时间复杂度L
                next_words.append(next_word)
    return next_words
