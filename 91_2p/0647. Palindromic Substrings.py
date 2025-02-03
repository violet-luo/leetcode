def countSubstrings(self, s: str) -> int:
    count = 0
    
    for mid in range(len(s)):
        count += self.extends_palindrome(s, mid, mid)
        count +=  self.extends_palindrome(s, mid, mid+1)
            
    return count
    
def extends_palindrome(self, s, low, high) -> int:
    count = 0
    while low >= 0 and high < len(s) and s[low] == s[high]:
        count += 1
        low -= 1 
        high += 1         
    return count
