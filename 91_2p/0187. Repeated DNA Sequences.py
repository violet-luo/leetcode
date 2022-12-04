def findRepeatedDnaSequences(self, s):
    counter = set()
    res = []
    
    for i in range(len(s) - 9):
        dna = s[i: i + 10]   
        if dna in counter and dna not in res: # ❌ "AAAAAAAAAAAAA" -> ["AAAAAAAAAA","AAAAAAAAAA","AAAAAAAAAA"]
            res.append(dna)
        else:
            counter.add(dna)
            
    return res
