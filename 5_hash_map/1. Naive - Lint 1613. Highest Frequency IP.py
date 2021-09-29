def highestFrequency(self, ipLines):
    mapdic = {}

    for ip in ipLines:
        if ip in mapdic:
            mapdic[ip] += 1
        else:
            mapdic[ip] = 1

    max = 0
    ans = ipLines[0]

    for key in mapdic:
        if int(mapdic[key]) > max: # '>' not supported between instances of 'int' and 'dict'
            max = mapdic[key]
            ans = key

    return ans
