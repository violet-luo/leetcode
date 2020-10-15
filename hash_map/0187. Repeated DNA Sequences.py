"""

Runtime: 52 ms, faster than 95.34% of Python3 online submissions for Repeated DNA Sequences.
Memory Usage: 26.2 MB, less than 5.98% of Python3 online submissions for Repeated DNA Sequences.

"""

def findRepeatedDnaSequences(self, s: str) -> List[str]:
    lst, res = set(), set()

    for i in range(len(s) - 9):
        seq = s[i:i+10]
        if seq not in res:
            if seq in lst:
                res.add(seq)
            else:
                lst.add(seq)

    return list(res)
