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
