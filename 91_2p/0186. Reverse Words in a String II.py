def reverseWords(self, s):
    self.reverse(s, 0, len(s) - 1)

    beg = 0
    for i in range(len(s)):
        # reverse word
        if s[i] == ' ':
            self.reverse(s, beg, i-1)
            beg = i + 1
        # reverse last word
        elif i == len(s) -1:
            self.reverse(s, beg, i)

def reverse(self, s, l, r):
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
