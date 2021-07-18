"""

Runtime: 32 ms, faster than 50.79% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 14.1 MB, less than 70.63% of Python3 online submissions for Excel Sheet Column Title.

Visualization: http://www.pythontutor.com/visualize.html#code=def%20convertToTitle%28n%29%3A%0A%20%20%20%20result%20%3D%20%5B%5D%0A%20%20%20%20while%20n%20%3E%200%3A%0A%20%20%20%20%20%20%20%20%23%20convert%20a%20char%20into%20its%20Unicode%0A%20%20%20%20%20%20%20%20%23%20ord%28'A'%29%20%3D%2065%0A%20%20%20%20%20%20%20%20result.append%28chr%28%28n-1%29%2526%20%2B%20ord%28'A'%29%29%29%0A%20%20%20%20%20%20%20%20print%28result%29%0A%20%20%20%20%20%20%20%20n%20%3D%20%28n%20-%201%29%20//%2026%0A%20%20%20%20%20%20%20%20print%28n%29%0A%20%20%20%20result.reverse%28%29%0A%20%20%20%20return%20''.join%28result%29%0A%20%20%20%20%0AconvertToTitle%28701%29&cumulative=false&curInstr=14&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

"""

def convertToTitle(self, n: int) -> str:
    result = []
    while n > 0:
        # convert a char into its Unicode
        # ord('A') = 65
        result.append(chr((n-1)%26 + ord('A')))
        n = (n - 1) // 26
    result.reverse()
    return ''.join(result)
