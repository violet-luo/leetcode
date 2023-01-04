"""

Runtime: 32 ms, faster than 62.62% of Python3 online submissions for Text Justification.
Memory Usage: 14.2 MB, less than 7.55% of Python3 online submissions for Text Justification.

"""

def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i%(len(cur)-1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(maxWidth)]
