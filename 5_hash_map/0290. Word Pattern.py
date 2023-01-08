def wordPattern(self, pattern, s):
    s = s.split(' ')
    if len(pattern) != len(s):
        return False

    p_to_s = collections.defaultdict(str)
    s_to_p = collections.defaultdict(str)

    for i in range(len(pattern)):
        if pattern[i] not in p_to_s:
            p_to_s[pattern[i]] = s[i]
        if s[i] not in s_to_p:
            s_to_p[s[i]] = pattern[i]
        if p_to_s[pattern[i]] != s[i] or s_to_p[s[i]] != pattern[i]:
            return False
    
    return True

###

def wordPattern(self, s, t):
    dic = {}
    t = t.split()
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] in dic:
            if dic[s[i]] != t[i]:
                return False
        elif t[i] in dic.values(): # 一定要加防止double matching # badc, baba
            return False
        else:
            dic[s[i]] = t[i]
    return True
