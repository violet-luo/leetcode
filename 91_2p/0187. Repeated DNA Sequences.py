def findRepeatedDnaSequences(s):
    counter = {}
    res = []
    
    for l in range(len(s) - 9):
        r = l + 10
        dna = s[l:r]
        counter[dna] = counter.get(dna, 0) + 1
        if counter[dna] == 2:
            res.append(dna)
    
    return res
