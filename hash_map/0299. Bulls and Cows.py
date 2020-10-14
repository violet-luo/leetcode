"""

Runtime: 40 ms, faster than 70.78% of Python3 online submissions for Bulls and Cows.
Memory Usage: 14.1 MB, less than 99.99% of Python3 online submissions for Bulls and Cows.

"""

def getHint(self, secret: str, guess: str) -> str:
    bull, cow = 0, 0
    s, g = {}, {}

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bull += 1
        else:
            s[secret[i]] = s.get(secret[i], 0) + 1
            g[guess[i]] = g.get(guess[i], 0) + 1

    for k in s:
        if k in g:
            cow += min(s[k], g[k])

    return '{0}A{1}B'.format(bull, cow)
