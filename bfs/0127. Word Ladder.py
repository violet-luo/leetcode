def ladderLength(self, start, end, dict):
    dict.add(end) #加终点进Dict
    queue = collections.deque([start]) 
    distance = {start: 1} #最后Return的结果要加1，不如放进去的时候就是1

    while queue: 
        word = queue.popleft()
        if word == end:
            return distance[word]

        # 如果不是终点，for循环它的邻居结点
        for next_word in self.get_next_words(word, dict):
            if next_word in distance:
                continue
            queue.append(next_word)
            distance[next_word] = distance[word] + 1
    return 0 #找不到的话

# 时间复杂度25L^2
def get_next_words(self, word, dict):
    words = []
    for i in range(len(word)): #时间复杂度Length
        left, right = word[:i], word[i+1:] #时间复杂度L
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if word[i] == char:
                continue
            next_word = left + char + right #时间复杂度L
            if next_word in dict: #时间复杂度L
                words.append(next_word)
    return words
