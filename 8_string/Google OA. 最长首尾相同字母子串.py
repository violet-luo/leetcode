def solution(S):
    d = {}
    # store the furthest index of the letters in S
    for i in range(len(S) - 1, -1, -1): #{b:7, a:6, c:0}
        if S[i] not in d:
            d[S[i]] = i
            
    max_length = float("-infinity")
    best_index = 0
    
    # loop from the beginning of S
    for i, let in enumerate(S): # (0, 'c')
        # calculate the distance from current instance of the letter to the last
        sub_length = d[let] + 1 - i
        # only update if the distance is greater than max
        # this means we always start our answer from the earliest index possible. 
        if sub_length > max_length:
            best_index = i
            max_length = sub_length
            
    return S[best_index:d[S[best_index]] + 1]
