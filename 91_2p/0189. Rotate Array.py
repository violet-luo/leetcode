def rotate(self, nums, k):
    k = k % len(nums)
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)

def reverse(self, s, l, r):
    while l < r:
        s[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
