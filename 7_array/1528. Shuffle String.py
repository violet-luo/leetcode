def restoreString(self, s, indices):
    length = len(s)
    res = [''] * length
    for i, ch in enumerate(s):
        res[indices[i]] = ch
    return "".join(res)
