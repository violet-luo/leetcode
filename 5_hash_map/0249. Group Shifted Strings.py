# {
#      (1, 1): ['abc', 'bcd', 'xyz'],  
#   (2, 2, 1): ['acef'],   
#       (25,): ['az', 'ba'],   
#          (): ['a', 'z']
# }

def groupStrings(self, strings):
    dic = {} # key: a tuple of diff between adjacent char
    for s in strings:
        key = ()
        for i in range(len(s) - 1):
            circular_difference = 26 + ord(s[i+1]) - ord(s[i])
            key += (circular_difference % 26,)
        dic[key] = dic.get(key, []) + [s]
    return list(dic.values())
