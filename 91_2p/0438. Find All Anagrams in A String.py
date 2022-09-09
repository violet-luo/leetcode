def findAnagrams(self, s, p):
    if len(p) > len(s):
        return []
    if p == s:
        return [0]
        
    p_hash, s_hash = {}, {}
    res = [] 

    # {'a':1, 'b':1, 'c':1}, {'c':1, 'b':1, 'a':1}
    for i in range(len(p)):
        p_hash[p[i]] = p_hash.get(p[i],0) + 1 
        s_hash[s[i]] = s_hash.get(s[i],0) + 1 
        
    if s_hash == p_hash:
        res.append(0)    
       
    for l in range(1, len(s) - len(p) + 1):
        r = l + len(p) - 1 
        # s_hash = {'c':1, 'b':1, 'a':1, 'e':1}
        s_hash[s[r]] = s_hash.get(s[r], 0) + 1 
        # s_hash = {'b':1, 'a':1, 'e':1}
        s_hash[s[l - 1]] -= 1 
        if s_hash[s[l - 1]] == 0:
            del s_hash[s[l -1]]
        
        if s_hash == p_hash:
            res.append(l)
            
    return res
