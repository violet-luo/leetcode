def restoreIpAddresses(self, s: str) -> List[str]:
    res, subset = [], []

    def is_valid(ip):
        if len(ip) > 1 and ip[0] == '0': return False
        if 0 <= int(ip) < 256: return True
        return False
    
    def backtrack(start_index):
        if len(subset) == 4 and start_index == len(s):
            return res.append('.'.join(subset[:]))
        for i in range(start_index, len(s)):
            if len(s) - start_index > 3*(4 - len(subset)): # 剪枝，剩下的字符串大于允许的最大长度则跳过
                continue
            substr = s[start_index: i + 1]
            if is_valid(substr):
                subset.append(substr)
            else:
                continue
            backtrack(i + 1)
            subset.pop()
    
    backtrack(0)
    return res
