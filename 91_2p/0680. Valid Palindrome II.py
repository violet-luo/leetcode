def validPalindrome(self, s):
        left = 0
        right = len(s) - 1 

        # edge case "a" 本身就是回文串
        if left >= right:
            return True

        while left <= right:
            if s[left] == s[right]:
                left += 1 
                right -= 1 
            else:
                # 碰到一对不符合，删除左边或右边的字符
                return self.helper(s, left, right - 1) or self.helper(s, left + 1, right)
        
        return True
                
                
    def helper(self, s, left, right):
        while left <= right:
            # 碰到第二对不符合，直接return False
            if s[left] != s[right]:
                return False 
        
            left += 1 
            right -= 1 
        
        return True
