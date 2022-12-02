❌❌❌
def twoSum(self, nums: List[int], target: int) -> List[int]:
    left, right = 1, len(nums)
    
    while left < right:
        two_sum = nums[left] + nums[right] # list index out of range
        if two_sum == target:
            return [left, right]
        elif two_sum > target:
            right -= 1
        else:
            left += 1

✅✅✅
def twoSum(self, nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    
    while left < right:
        two_sum = nums[left] + nums[right]
        if two_sum == target:
            return [left + 1, right + 1]
        elif two_sum > target:
            right -= 1
        else:
            left += 1
