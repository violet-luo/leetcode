def reverseWords(self, s: str) -> str:
    res = ""
    s = " " + s + " "
    l = r = -1
    
    for i in range(len(s) - 2, 0, -1):
        # end of word
        if s[i] != " " and s[i + 1] == " ":
            r = i
        if s[i - 1] == " " and s[i] != " ":
            l = i
            res += " " + s[l: r + 1]
    return res[1:]
