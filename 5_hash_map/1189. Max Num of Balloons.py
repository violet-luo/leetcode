def maxNumberOfBalloons(self, text):
    counter = collections.Counter(text)
    res = min(counter['b'], counter['a'], counter['l'] // 2, counter['o'] // 2, counter['n'])
    return res
