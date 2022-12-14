def countLetters(self, S: str) -> int:
    count = total = 0
    
    for i in range(len(S)):
        if S[i - 1] and S[i] == S[i - 1]:
            count += 1
        else:
            count = 1
        total += count
        
    return total
