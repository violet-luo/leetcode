def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    s_to_t = collections.defaultdict(str)
    t_to_s = collections.defaultdict(str)

    for i in range(len(s)):
        if s[i] not in s_to_t:
            s_to_t[s[i]] = t[i]
        if t[i] not in t_to_s:
            t_to_s[t[i]] = s[i]
        if s_to_t[s[i]] != t[i] or t_to_s[t[i]] != s[i]:
            return False
    return True

###

def isIsomorphic(self, s: str, t: str) -> bool:
    dic = {}

    for i in range(len(s)):
        if s[i] in dic:
            if dic[s[i]] != t[i]:
                return False
        elif t[i] in dic.values():
            return False
        else:
            dic[s[i]] = t[i] #'e' = 'a'
    return True
