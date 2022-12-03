def rotate(self, nums, k): # 1 2 3 4 5 6 7
    n = len(nums)
    k = k % n
    self.reverse(nums, 0, n - 1) # 7 6 5 4 3 2 1
    self.reverse(nums, 0, k - 1) # reverse the first k num, 5 6 7 4 3 2 1
    reverse(nums, k, n - 1) # reverse last n - k num, 5 6 7 1 2 3 4

def reverse(self, s, left, right):
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
