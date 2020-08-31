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
