"""

Runtime: 32 ms, faster than 72.34% of Python3 online submissions for Simplify Path.
Memory Usage: 14.1 MB, less than 15.49% of Python3 online submissions for Simplify Path.

"""

def simplifyPath(self, path: str) -> str:
    places = [p for p in path.split("/") if p!="." and p!=""]
    stack = []
    for p in places:
        if p == "..":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(p)
    return "/" + "/".join(stack)
