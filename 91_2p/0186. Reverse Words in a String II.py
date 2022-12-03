def reverseWords(self, s):
    self.reverse(s, 0, len(s) - 1)

    first_idx = 0 # first index of the current word
    for cur_idx in range(len(s)):
        if s[cur_idx] == ' ': # reverse word
            self.reverse(s, first_idx, cur_idx - 1)
            first_idx = cur_idx + 1
        elif cur_idx == len(s) - 1: # reverse the last word, cause there's no space after 
            self.reverse(s, first_idx, cur_idx)

def reverse(self, s, l, r):
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
