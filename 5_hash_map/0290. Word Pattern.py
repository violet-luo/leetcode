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
