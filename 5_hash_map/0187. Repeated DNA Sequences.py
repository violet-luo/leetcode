def findRepeatedDnaSequences(self, s: str) -> List[str]:
    seen = set()
    res = []

    for i in range(len(s) - 9): # s长度为11,range(0,1)
        substr = s[i:i+10]
        if substr in seen and substr not in res:
            res.append(substr)
        else:
            seen.add(substr)
    
    return res

###

def findRepeatedDnaSequences(self, s):
    seen = set()
    res = set()
    
    for i in range(len(s) - 9): # 假设s长度为10,range(0,1)
        seq = s[i:i+10]
        if seq in seen:
            res.add(seq)
        else:
            seen.add(seq)

    return list(res)
