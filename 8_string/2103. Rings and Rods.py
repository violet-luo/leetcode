def countPoints(rings):
    count = 0
    l = [""]*10
    for i in range(1,len(rings), +2): # ['','','BGR']
        l[int(rings[i])] += rings[i - 1]
    for j in l:
        if 'R' in j and 'G' in j and 'B' in j:
            count += 1
    return count
