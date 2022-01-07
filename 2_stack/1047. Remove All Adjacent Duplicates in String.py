def removeDuplicates(s):
    res = []
    
    for char in s:
        if res and res[-1] == c:
            res.pop()
        else:
            res.append()
    return "".join(res)
