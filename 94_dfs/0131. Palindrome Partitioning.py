def partition(self, s):
    res = []  
    subset = []

    def backtrack(s, start_index):
        if start_index >= len(s):  # 递归终止条件
            return res.append(subset[:])
        for i in range(start_index,len(s)):
            substring = s[start_index : i + 1]
            if substring == substring[::-1]: 
                subset.append(substring)
            else:   # 不包含的话，会pop from empty list
                continue
            backtrack(s, i+1)  #寻找i+1为起始位置的子串
            subset.pop()

    backtrack(s,0)
    return res

###

def partition(self, s):
    res, subset = [], []  
    self.backtrack(s, 0, res,subset)
    return res

def backtrack(self, s, start_idx, res, subset):
    if start_idx >= len(s):  #如果起始位置已经大于s的大小，说明已经找到了一组分割方案了
        return res.append(subset[:])
    for i in range(start_idx, len(s)):
        p = s[start_idx : i + 1]  #获取[start_idx,i+1]在s中的子串
        if p == p[::-1]: 
            subset.append(p)
        else: 
            continue 
        self.backtrack(s, i+1, res, subset)  #寻找i+1为起始位置的子串
        subset.pop()  #回溯过程，弹出本次已经填在path的子串
