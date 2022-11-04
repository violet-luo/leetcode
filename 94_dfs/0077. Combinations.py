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
