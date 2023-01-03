def sortIntegers(self, nums): #[5,4,3,2,1]
    self.quickSort(nums, 0, len(nums) - 1)

def quickSort(self, nums, start, end):
    if start >= end:
        return
    
    left, right = start, end
    # key point 1: pivot is value, not index
    pivot = nums[(start + end) // 2]

    # key point 2: left <= right not left < right
    while left <= right:
        while left <= right and nums[left] < pivot: # left最后会走到index 3
            left += 1
        while left <= right and nums[right] > pivot: # right最后会走到index 1
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    self.quickSort(nums, start, right)
    self.quickSort(nums, left, end)
