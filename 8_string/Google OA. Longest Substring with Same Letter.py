def solution(s):
    dict = {}
    # store the furthest index of the letters in S
    for i in range(len(s) - 1, -1, -1): # {b:7, a:6, c:0}
        if s[i] not in dict:
            dict[s[i]] = i
            
    max_len, min_idx = 0, 0

    # loop from the beginning of S
    for idx, letter in enumerate(s): # (0, 'c')
        # calculate the distance from current instance of the letter to the last
        substr_len = dict[letter] + 1 - idx
        # only update if the distance is greater than max
        # this means we always start our answer from the earliest index possible. 
        if substr_len > max_len:
            min_idx = idx
            max_len = substr_len
            
    return s[min_idx : dict[s[min_idx]] + 1]
