def groupAnagrams(strs):
    dic = {}

    for str in strs: # eat
        key_str = ''.join(sorted(str)) # ate
        if key_str in dic:
            dic[key_str].append(str)
        else:
            dic[key_str] = [str]
    return list(dic.values())
