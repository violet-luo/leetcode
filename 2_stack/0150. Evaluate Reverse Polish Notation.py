"""

Runtime: 68 ms, faster than 80.02% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 14 MB, less than 87.41% of Python3 online submissions for Evaluate Reverse Polish Notation.

"""

def evalRPN(self, tokens: List[str]) -> int:
    stack = []

    for t in tokens:
        if t not in ["+", "-", "*", "/"]:
            stack.append(int(t))
        else:
            # test case ["4","3","-"]
            b, a = stack.pop(), stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                if a * b < 0 and a % b != 0:
                    stack.append(a//b+1)
                else:
                    stack.append(a//b)
    return stack.pop()
