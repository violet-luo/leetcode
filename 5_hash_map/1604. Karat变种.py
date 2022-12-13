def timeChange(time):
    if len(time) == 4:
        hour = int(time[:2])
        mins = int(time[2:])
    if len(time) == 3:
        hour = int(time[0])
        mins = int(time[1:])
    if len(time) <= 2:
        hour = 0
        mins = int(time)
    return hour*60 +mins
    
def badgeTime(badge_times):
    dic = defaultdict(list)
    for name, time in badge_times:
        dic[name].append(time)
    res = {}
    for name in dic:
        for i, time in enumerate(sorted(dic[name], key = lambda x: timeChange(x))):
            cand = [time]
            for j in sorted(dic[name], key = lambda x: timeChange(x))[i+1:]:
                if timeChange(j)- timeChange(time) <= 60:
                    cand.append(j)
                else:
                    break
            if len(cand) >= 3:
                res[name] = cand
                break
                
    return res
