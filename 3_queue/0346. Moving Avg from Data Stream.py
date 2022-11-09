class MovingAverage:
    def __init__(self, size):
        self.queue = deque([])
        self.size = size # window size 3
        self.sum = 0.0

    def next(self, val):
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()
            
        self.sum += val
        self.queue.append(val)
        return self.sum / len(self.queue) # 不能是self.size
