def alertNames(keyName, keyTime):
    converted_time = []

    for time in keyTime:
        split = time.split(':')
        hr = int(split[0])
        mins = int(split[1])
        converted_time.append(hr * 60 + mins)

    dic = {}

    for i in range(len(keyName)):
        name = keyName[i]
        time = converted_time[i]
        if name in dic:
            dic[name].append(time)
        else:
            dic[name] = [time]

    sorted_dic = {k: sorted(v) for k,v in dic.items()}

    # for name in dic.keys():
    #     dic[name].sort()

    res = []

    for name in sorted_dic:
        for i in range(len(sorted_dic[name]) - 2):
            if 0 < sorted_dic[name][i + 2] - sorted_dic[name][i] <= 60:
                res.append(name)
                break
    res.sort()
    return res
