def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    cnt = 0
    
    for i in range(len(s)):
        if g[cnt] <= s[i]:
            cnt += 1
        if cnt >= len(g):
            break
    return cnt 
  
  ###
  
  def findContentChildren(self, g, s):
    g.sort()
    s.sort()
    cnt = 0

    for i in range(len(s)):
        if cnt < len(g) and s[i] >= g[cnt]:
            cnt += 1
    return cnt
