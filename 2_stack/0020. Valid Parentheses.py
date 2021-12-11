"""

Runtime: 52 ms, faster than 18.00% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14 MB, less than 21.80% of Python3 online submissions for Valid Parentheses.

https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack

"""

def isValidParentheses(self, s):
    stack = []
    dict = {")":"(", "}":"{", "]":"["}

    for bracket in s:
        # open brackets
        if bracket in dict.values():
            stack.append(bracket)
        # closed brackets
        elif bracket in dict.keys():
            # if pop closed brackets while stack is null, then return false
            # if closed bracket != open bracket, then return false
            if stack == [] or dict[bracket] != stack.pop():
                return False

    return stack == []

"""

Amazon OA
给你一个str,里面只有 '('和‘)’,让你数valid pairs一共有多少,如果不是valid就返回-1.

"""
def isValid(s):
    stack = []
    counter = 0

    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) > 0:
                stack.pop()
                counter += 1
        else:
            return -1
        
    if len(stack) == 0:
        return counter
    else:
        return -1
