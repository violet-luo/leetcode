def removeDuplicates(self, s):
    res = []

    for char in s:
        if res and res[-1] == char:
            res.pop()
        else:
            res.append(char)
    return "".join(res)
