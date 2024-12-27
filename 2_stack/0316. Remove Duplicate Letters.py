def removeDuplicateLetters(self, s: str) -> str:
    seen = set() # 记录当前栈中已存在的字符，time O(1), 比在stack中查看时间复杂度更优
    stack = []
    char_last_occurence = {char: idx for idx, char in enumerate(s)} # {'c': 7, 'b': 6, 'a': 2, 'd': 4}
    
    for idx, char in enumerate(s):
        if char in seen:
            continue
        
        # 如果栈顶元素比当前元素大，且栈顶元素后面还会出现，则弹出栈顶
        # 当出现更小的字符时，移除栈顶较大的字符（前提是这些字符后续还会出现），从而使字典序更小。
        # stack = [c], seen = {c}
        # b不在seen中，b比栈顶c小，且c后面还会出现，弹出c, 加入b, stack = [b], seen = {b}
        # 同理，弹出b, 加入a, stack = [a], seen = {a}
        # c不在seen中，加入c, stack = [a,c] seen = {a,c}
        # d不在seen中，加入d, stack = [a,c,d] seen = {a,c,d}
        while stack and char < stack[-1] and char_last_occurence[stack[-1]] > idx:
            removed_char = stack.pop()
            seen.remove(removed_char)
        
        stack.append(char)
        seen.add(char)
    
    return ''.join(stack)
