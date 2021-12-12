def unique_files(filenames):
    dic = {}
    res = []

    for file in filenames:
        if file in dic:
            dic[file] += 1
            res.append(file + str(dic[file]))
        else:
            dic[file] = 0
            res.append(file)
    return res
