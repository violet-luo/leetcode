def balancedStringSplit(self, s: str) -> int:
    count = 0
    flag = 0
    for i in s:
        if i == 'R':
            flag += 1
        else:
            flag -= 1
        if flag == 0:
            count += 1
    return count
