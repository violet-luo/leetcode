def getHint(self, secret: str, guess: str) -> str:
    bulls, cows = 0, 0
    secret_count, guess_count = collections.defaultdict(int), collections.defaultdict(int) # 不能写 secret_count = guess_count = collections.defaultdict(int) or they will refer to the same dict

    for i in range(len(secret)): # guess might not be long enough
        if secret[i] == guess[i]:
            bulls += 1
        else:
            secret_count[secret[i]] += 1
            guess_count[guess[i]] += 1

    for g in guess_count:
        if g in secret_count:
            cows += min(secret_count[g], guess_count[g])
    
    return f"{bulls}A{cows}B"
