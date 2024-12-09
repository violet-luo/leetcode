def twoSum(self, numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i in range(n):
        diff = target - numbers[i]
        l, r = i + 1, n - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if numbers[mid] == diff:
                return [i + 1, mid + 1]
            elif numbers[mid] < diff:
                l = mid
            else:
                r = mid
        if numbers[l] == diff:
            return [i + 1, l + 1]
        if numbers[r] == diff:
            return [i + 1, r + 1]
                
###

def twoSum(self, nums: List[int], target: int) -> List[int]:
    left, right = 0, 0
    for left in range(len(nums) - 1): 
        right = self.found_right(nums, left, target - nums[left])
        if right:
            return [left + 1, right + 1]
    return None

def found_right(self, nums, left, target):
    start, end = left + 1, len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid
        else:
            end = mid

    if nums[start] == target:
        return start
    if nums[end] == target:
        return end        

    return None

###

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i in range(n):
        start, end = i + 1, n - 1
        while start <= end:
            mid = (start + end) // 2
            if numbers[mid] == target - numbers[i]:
                return [i + 1, mid + 1]
            elif numbers[mid] > target - numbers[i]:
                end = mid - 1
            else:
                start = mid + 1

    return [-1, -1]
