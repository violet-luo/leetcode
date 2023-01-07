def toLowerCase(self, s: str) -> str:
    res = ''
    for c in s:
        if 65 <= ord(c) <= 90: # 不能只是 < 97, 还有非字母字符
            res += chr(ord(c) + 32)
        else:
            res += c
    return res
