def firstUniqChar(self, str):
    counter = {}

    for c in str:
        counter[c] = counter.get(c, 0) + 1

    for c in str:
        if counter[c] == 1:
            return c
