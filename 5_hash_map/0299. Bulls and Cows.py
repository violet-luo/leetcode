def getHint(secret, guess):
    bull, cow = 0, 0
    s, g = {}, {}

    for i in range(len(secret)):
        if secret[i] == guess[i]: # '1'
            bull += 1
        else:
            s[secret[i]] = s.get(secret[i], 0) + 1 # {'1':1, '2':1, '3':1}
            g[guess[i]] = g.get(guess[i], 0) + 1 # {'0':1, '1':2}

    for k in s: # '1'
        if k in g:
            cow += min(s[k], g[k]) # 1

    return '{0}A{1}B'.format(bull, cow)
