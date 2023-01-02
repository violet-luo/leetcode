def combinationSum(self, candidates, target):
    res, subset = [], []
    candidates = sorted(candidates) # 不知道为什么不sort过不了

    def backtrack(start_index, sum):
        if sum > target:
            return 
        if sum == target:
            return res.append(subset[:])
        
        for i in range(start_index, len(candidates)):
            if sum + candidates[i] > target:
                return 
            sum += candidates[i]
            subset.append(candidates[i])
            backtrack(i, sum)
            sum -= candidates[i]
            subset.pop()
    
    backtrack(0, 0)
    return res

###

def combinationSum(self, candidates, target):
    res, subset = [], []
    candidates = sorted(candidates)  #需要排序
    self.backtrack(candidates, target, 0, 0, res, subset)
    return res

def backtrack(self, candidates, target, sum, start_idx, res, subset):
    if sum > target: 
        return 
    if sum == target: 
        return res.append(subset[:])
    for i in range(start_idx, len(candidates)):
        if sum + candidates[i] > target: 
            return
        sum += candidates[i] 
        subset.append(candidates[i])
        self.backtrack(candidates, target, sum, i, res, subset)  #start_idx = i:表示可以重复读取当前的数
        sum -= candidates[i]  #回溯
        subset.pop()  #回溯
