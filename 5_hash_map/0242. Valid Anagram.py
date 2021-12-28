def isAnagram(self, s, t):
    dic = {}
    
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    for j in t:
        if j not in dic:
            return False
        else:
            dic[j] -= 1
    
    for val in dic.values():
        if val != 0:
            return False
    
    return True

def isAnagram(self, s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2

def isAnagram(self, s, t):
    return sorted(s) == sorted(t)
