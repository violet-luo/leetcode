"""

Runtime: 24 ms, faster than 97.22% of Python3 online submissions for Add Binary.
Memory Usage: 14.2 MB, less than 6.70% of Python3 online submissions for Add Binary.

"""

def addBinary(self, a: str, b: str) -> str:
    carry = 0
    result = ''

    a = list(a)
    b = list(b)

    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())

        result += str(carry %2)
        carry //= 2

    return result[::-1]
