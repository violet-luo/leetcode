def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res, subset = [], []
    candidates.sort() #不sort的话 [8,7,4,3] target = 11会直接fail
    
    def backtrack(start_index, total):
        if total > target:
            return 
        if total == target:
            res.append(subset[:])
        
        for i in range(start_index, len(candidates)):
            if total + candidates[i] > target:
                return 
            total += candidates[i]
            subset.append(candidates[i])
            backtrack(i, total)
            total -= candidates[i]
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
