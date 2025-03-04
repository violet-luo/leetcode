def minLength(self, s: str, numOps: int) -> int:
    groupings = []
    current_group_size = 0
    current_group_char = None
    for c in s:
        if current_group_char is None:
            current_group_size = 1
            current_group_char = c
            continue
        if c != current_group_char:
            groupings.append(current_group_size)
            current_group_size = 1
            current_group_char = c
        else:
            current_group_size += 1
    groupings.append(current_group_size)
    

    def check(k):
        # edge case k == 1: 010101 or # 101010
        if k == 1:
            starter = False
            needed = 0
            for c in s:
                if starter:
                    if c == "0":
                        needed += 1
                else:
                    if c == "1":
                        needed += 1
                starter = not starter
            return min(needed, len(s) - needed) <= numOps
        
        # [5, 1] 00000 takes 1 flip to has substring with at most two '0'
        return sum(g//(k + 1) for g in groupings) <= numOps 

    l = 1
    r = len(s)
    while l < r:
        mid = (l + r) // 2
        if check(mid): # use binary search to find the smallest valid k
            r = mid
        else:
            l = mid + 1
    return l
