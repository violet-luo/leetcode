def combinationSum3(self, k, n):
    res, subset = [], []

    def backtrack(start_index, sum):
        if sum > n: 
            return
        if sum == n and len(subset) == k:
            return res.append(subset[:])
        for i in range(start_index, 9 - (k - len(subset)) + 2): #剪枝
            sum += i
            subset.append(i)
            backtrack(i + 1, sum)
            sum -= i
            subset.pop()

    backtrack(1, 0)
    return res

### 
 
def combinationSum3(self, k, n):
    res, subset = [], []
    self.backtrack(n, k, 0, 1, res, subset)
    return res

def backtrack(self, n, k, sum, start_idx, res, subset):
    if sum > n: 
        return
    if sum == n and len(subset) == k:  #如果subset.size() == k 但sum != n 直接返回
        return res.append(subset[:])
    for i in range(start_idx, 9 - (k - len(subset)) + 2):  #剪枝操作
        subset.append(i)
        sum += i 
        self.backtrack(n, k, sum, i + 1, res, subset)  #注意i+1调整start_idx
        sum -= i  #回溯
        subset.pop()  #回溯
