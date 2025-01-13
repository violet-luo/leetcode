def reverseWords(self, s: str) -> str:
    s = s.strip()
    n = len(s)
    s = list(s)

    # 1. reverse the whole list
    self.reverse(s, 0, n - 1)
    print(s)

    # 2. reverse each word
    s.append(' ')
    l = 0
    for r in range(n + 1):
        if s[r] == ' ':
            self.reverse(s, l, r - 1)
            l = r + 1

    # 3. remove extra space
    self.remove_extra_space(s)
    s.pop(-1)
    return ''.join(s)


def reverse(self, s, l, r):
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

def remove_extra_space(self, s):
    i = 1
    while i < len(s):
        if s[i] == ' ' and s[i - 1] == ' ':
            s.pop(i)
        else:
            i += 1
 
###

def reverseWords(self, s: str) -> str:
    s = s.strip()
    s = list(s)

    self.reverse(s, 0, len(s) - 1)

    l = 0
    for r in range(len(s) + 1):
        if r == len(s) or s[r] == " ":
            self.reverse(s, l, r - 1)
            l = r + 1
    
    self.remove_extra_space(s)

    return "".join(s)

def reverse(self, word, l, r):
    while l < r:
        word[l], word[r] = word[r], word[l]
        l += 1
        r -= 1

def remove_extra_space(self, words:list): # "a good   example"
    # can't use for loop here because after popping elements list shrinks
    # 也不可以用 n = len(words), while i < n
    i = 1
    while i < len(words):
        if words[i] == " " and words[i - 1] == " ":
            words.pop(i)
        else:
            i += 1

###

def reverseWords(self, s: str) -> str:
    res = ""
    s = " " + s + " "
    l = r = -1
    
    for i in range(len(s) - 2, 0, -1):
        # end of word
        if s[i] != " " and s[i + 1] == " ":
            r = i
        if s[i - 1] == " " and s[i] != " ":
            l = i
            res += " " + s[l: r + 1]
    return res[1:]
