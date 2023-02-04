def reverseWords(s):
    reverse(s, 0, len(s) - 1) # [eulb si yks eht]

    first_idx = 0 # first index of the current word
    for cur_idx in range(len(s)):
        # reverse words but the last
        if s[cur_idx] == ' ':
            reverse(s, first_idx, cur_idx - 1)
            first_idx = cur_idx + 1
        # revesrse the last word
        elif cur_idx == len(s) - 1: 
            reverse(s, first_idx, cur_idx)

def reverse(s, l, r):
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
