def combine(n, k):
    res, subset = [], []

    def backtrack(start_index):
        if len(subset) == k: # 与78的区别
            return res.append(subset[:])
        for i in range(start_index, n - (k - len(subset)) + 2): # 剪枝
            subset.append(i) # 与78的区别，不需要append所有的子集
            backtrack(i + 1)
            subset.pop()
            
    backtrack(1)
    return res 

###

def combine(self, n, k):
    res, subset = [], []
    self.backtrack(n, k, 1, res, subset)
    return res

def backtrack(self, n, k, start_idx, res, subset):
    if len(subset) == k:
        res.append(subset[:])
        return
    for i in range(start_idx, n - (k - len(subset)) + 2):
        subset.append(i)
        self.backtrack(n, k, i + 1, res, subset)
        subset.pop()
