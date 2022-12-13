def longest_url(user0, user1):
    m = len(user0)
    n = len(user1)

    res = []
    max_count = 0

    for i in range(m):
        for j in range(n):
            if user0[i] == user1[j]:
                sublen = 1 #公共子序列长度至少为1 
                subarr = []
                while i + sublen < m and j + sublen < n and user0[i + sublen] == user1[j + sublen]:
                    sublen += 1
                    subarr = user0[i:i+sublen]
                if sublen > max_count:
                    max_count = max(max_count, sublen)
                    res = subarr
                    
    return res
