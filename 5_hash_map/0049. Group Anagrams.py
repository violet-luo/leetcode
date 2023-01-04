def groupAnagrams(self, strs):
    dic = collections.defaultdict(list)
    for str in strs:
        sorted_str = ''.join(sorted(str))
        dic[sorted_str].append(str)
    return list(dic.values())
