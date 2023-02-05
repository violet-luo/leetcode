def findContentChildren(self, g, s):
    g.sort()
    s.sort()
    m, n = len(g), len(s)
    g_idx, s_idx, count = 0, 0, 0

    while g_idx < m and s_idx < n:
        if s[s_idx] >= g[g_idx]: # 当前饼干可以满足孩子
            count += 1
            g_idx += 1
            s_idx += 1
        else:
            s_idx += 1
    
    return count
