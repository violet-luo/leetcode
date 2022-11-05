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
