def combine(self, n: int, k: int) -> List[List[int]]:
    res, combination = [], []
    
    def backtrack(start_index):
        if len(combination) == k:
            return res.append(subset[:])
        for i in range(start_index, n - (k - len(combination)) + 2): #剪枝
            combination.append(i)
            backtrack(i + 1)
            combination.pop()
    
    backtrack(1) # range from 1
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
