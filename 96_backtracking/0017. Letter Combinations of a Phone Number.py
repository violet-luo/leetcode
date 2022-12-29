map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
class Solution:
    def letterCombinations(self, digits):
        res, subset = [], []
        if not digits:
            return res

        def backtrack(start_index):
            if start_index == len(digits):
                return res.append(''.join(subset)) # 要['ad']而不是['a','d']
            
            letters = map[digits[start_index]]
            for letter in letters:
                subset.append(letter)
                backtrack(start_index + 1)
                subset.pop()
        
        backtrack(0)
        return res

###

map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

class Solution:    
    def letterCombinations(self, digits):
        char, res = '', []
        if digits == '':
            return res
        self.backtrack(digits, 0, char, res)
        return res

    def backtrack(self, digits, index, char, res):
        if index == len(digits):
            res.append(char)
            return
        
        letters = map[digits[index]]
        for letter in letters:
            char += letter
            self.backtrack(digits, index + 1, char, res)
            char = char[:-1] # 回溯
