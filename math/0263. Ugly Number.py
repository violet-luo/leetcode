"""

Sucession of No.231. Power of Two

Runtime: 28 ms, faster than 86.73% of Python3 online submissions for Ugly Number.
Memory Usage: 14.1 MB, less than 99.95% of Python3 online submissions for Ugly Number.

"""

def isUgly(self, num: int) -> bool:
    if num == 0:
        return False
    while num % 2 == 0:
        num /= 2
    while num % 3 == 0:
        num /= 3
    while num % 5 == 0:
        num /= 5
    return num == 1
