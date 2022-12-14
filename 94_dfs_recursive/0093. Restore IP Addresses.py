def restoreIpAddresses(self, s):
    res = []
    subset = [] 

    def is_valid(ip):
        if len(ip) > 1 and ip[0] == '0': return False
        if 0 <= int(ip) < 256: return True
        return False

    def backtrack(s, start_index):
        if len(s) > 12: return
        if len(subset) == 4 and start_index == len(s):
            res.append(".".join(subset[:]))
            return

        for i in range(start_index, len(s)):
            if len(s) - start_index > 3*(4 - len(subset)): continue # 剪枝，剩下的字符串大于允许的最大长度则跳过
            substr = s[start_index : i + 1]
            if is_valid(substr):
                subset.append(substr)
            else: 
                continue
            backtrack(s, i + 1)
            subset.pop()

    backtrack(s, 0)
    return res

###

def restoreIpAddresses(self, s):
    res, subset = [], []
    self.backtrack(s, 0, res, subset)
    return res

def backtrack(self, s, start, res, subset): 
    if len(subset) == 4 and start == len(s):
        res.append(".".join(subset))
        return

    for i in range (1,4):
        if start + i > len(s):
            continue
        if self.isValid(s[start : start + i]):
            subset.append(s[start : start + i])
            self.backtrack(s, start + i, res, subset)
            subset.pop()

def isValid(self, s):
    if len(s) > 1 and s[0] == "0":
        return False
    if 0 <= int(s) <= 255:
        return True
    return False
