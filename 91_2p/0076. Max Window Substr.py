def minWindow(self, s: str, t: str) -> str:
    t_dic = collections.Counter(t)
    s_dic = collections.defaultdict(int)
    len_t = len(t)
    min_len = float('inf')
    res = ""
    valid_chars = 0 # 记录s中大于等于t中的字符数

    l = 0
    for r in range(len(s)):
        s_dic[s[r]] += 1

        # 如果 s[r] 是 t 中的字符且刚好满足 t 的需求
        if s[r] in t_dic and t_dic[s[r]] == s_dic[s[r]]:
                valid_chars += 1
        
        # 当所有字符种类的需求都满足时
        while len(t_dic) == valid_chars:
            if min_len > r - l + 1:
                min_len = r - l + 1
                res = s[l:r + 1]
            
            if s[l] in t_dic and t_dic[s[l]] == s_dic[s[l]]:
                valid_chars -= 1

            s_dic[s[l]] -= 1
            l += 1
    return res
