def longestCommonPrefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len) #'flow'
    for i, ch in enumerate(shortest): # o, 'f'
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest 
