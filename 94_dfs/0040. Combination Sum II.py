def combinationSum(self, candidates, target):
    res = []
    subset = []
    sum = 0

    def backtrack(candidates, target, sum, start_index):
        if sum == target:
            return res.append(subset[:])
        for i in range(start_index, len(candidates)):
            if i > start_index and candidates[i] == candidates[i - 1]: #与39区别，去重
                continue
            if sum + candidates[i] > target:
                return 
            sum += candidates[i]
            subset.append(candidates[i])
            backtrack(candidates, target, sum, i)
            sum -= candidates[i]
            subset.pop()

    candidates = sorted(candidates) # 不知道为什么不sort过不了
    backtrack(candidates, target, 0, 0)
    return res

###

def combinationSum2(self, candidates, target):
    res, subset = [], []
    candidates = sorted(candidates)  # 给candidates排序，让相同的元素都挨在一起
    self.backtrack(candidates, target, 0, 0, res, subset)
    return res

def backtrack(self, candidates, target, sum, start_idx, res, subset):
    if sum == target: 
        res.append(subset[:])
    for i in range(start_idx,len(candidates)):  #要对同一树层使用过的元素进行跳过
        if sum + candidates[i] > target: 
            return 
        if i > start_idx and candidates[i] == candidates[i-1]: #与39唯一不同
            continue  #直接用start_idx来去重,要对同一树层使用过的元素进行跳过
        sum += candidates[i]
        subset.append(candidates[i])
        self.backtrack(candidates, target, sum, i+1, res, subset)  #i+1:每个数字在每个组合中只能使用一次
        sum -= candidates[i]  #回溯
        subset.pop()  #回溯
