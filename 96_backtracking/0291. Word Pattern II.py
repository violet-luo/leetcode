def wordPatternMatch(self, pattern, string):
    return self.is_match(pattern, string, {}, set())

def is_match(self, pattern, string, dic, seen):
    if not pattern:
        return not string
        
    char = pattern[0]

    # 1. 如果当前模板的字母已经有匹配过字符串word
    if char in dic:
        word = dic[char]
        # char对应的word当前无法和str的前缀匹配
        # 例如模板为ABA，字符串为abc，则搜索到第三位时A已经匹配过a，但现在str中是c无法匹配
        if not string.startswith(word): 
            return False
        # pattern往后1位，str往后word的长度位数
        return self.is_match(pattern[1:], string[len(word):], dic, seen)
    
    # 2. 如果当前模板的字母未匹配过字符串
    for i in range(len(string)):
        word = string[:i + 1]
        # 确保pattern中不同的char对应不同的word，剪枝
        if word in seen:
            continue
        
        seen.add(word)
        dic[char] = word
        
        if self.is_match(pattern[1:], string[i + 1:], dic, seen):
            return True
        
        del dic[char]
        seen.remove(word)
        
    return False
