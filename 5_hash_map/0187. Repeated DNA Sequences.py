def findRepeatedDnaSequences(self, s):
    dic = {}
    res = []
    
    for i in range(len(s) - 9): # 假设s长度为10,range(0,1)
        seq = s[i:i+10]
        if seq in dic:
            dic[seq] += 1
        else:
            dic[seq] = 1
    
    for seq in dic:
        if dic[seq] > 1:
            res.append(seq)

    return res
  
def findRepeatedDnaSequences(self, s):
    dic = set()
    res = set()
    
    for i in range(len(s) - 9): # 假设s长度为10,range(0,1)
        seq = s[i:i+10]
        if seq in dic:
            res.add(seq)
        else:
            dic.add(seq)

    return list(res)
