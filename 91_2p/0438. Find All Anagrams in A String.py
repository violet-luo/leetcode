def findAnagrams(self, s: str, p: str) -> List[int]:
    p_dic = collections.Counter(p)
    s_dic = collections.defaultdict(int)
    res = []

    l = 0
    for r in range(0, len(s)):
        s_dic[s[r]] += 1
        if r - l + 1 == len(p):
            if s_dic == p_dic:
                res.append(l)
            s_dic[s[l]] -= 1
            if s_dic[s[l]] == 0:
                del s_dic[s[l]]
            l += 1
    
    return res
