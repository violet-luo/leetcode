"""

Runtime: 92 ms, faster than 94.53% of Python3 online submissions for Group Anagrams.
Memory Usage: 16.6 MB, less than 6.77% of Python3 online submissions for Group Anagrams.

"""

def groupAnagrams(strs):
    dic = {}

    for str in strs:
        key_str = ''.join(sorted(str))
        if key_str in dic:
            dic[key_str].append(str)
        else:
            dic[key_str] = [str]
    return list(dic.values())
