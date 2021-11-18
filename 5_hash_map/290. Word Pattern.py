def wordPattern(self, pattern, s):
    dic = {}
    s = s.split()

    for i in range(len(pattern)):
        if pattern[i] in dic:
            if dic[pattern[i]] != s[i]:
                return False
        elif s[i] in dic.values(): #if s[i] is already matched with
            return False
            dic[pattern[i]] = s[i]
        else:
            dic[pattern[i]] = s[i]
    return True
