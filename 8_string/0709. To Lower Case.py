def toLowerCase(self, s):
    res = ""
    for c in s:
        n = ord(c)
        res += chr(n + 32) if 65 <= n <= 90 else c
    return res
