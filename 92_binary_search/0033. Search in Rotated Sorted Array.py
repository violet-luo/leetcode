# 1. Two binary searches
def search(self, nums: List[int], target: int) -> int:
    # 1. find index of min
    n = len(nums)
    l, r = 0, n - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid
        else:
            r = mid
    num_min_idx = l if nums[l] < nums[r] else r

    # 2.
    if target <= nums[-1]:
        return self.binary_search(nums, num_min_idx, n - 1, target)
    else:
        return self.binary_search(nums, 0, num_min_idx - 1, target)

def binary_search(self, nums, l, r, target):
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid 
        else:
            r = mid
    
    if nums[l] == target:
        return l
    if nums[r] == target:
        return r
        return -1

# 2. One binary search
def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]: # 在左边
            # 不能是 nums[mid] > target
            # [4, 5, 6, 7, 0, 1, 2]，nums[mid] might be 7
            # nums[mid] > target always hold true, 不知道是往左还是往右
            # 要带等号，array没有重复值，但是target可能会相等
            if nums[l] <= target <= nums[mid]:
                r = mid
            else:
                l = mid
        else: # 在右边
            if nums[mid] <= target <= nums[r]:
                l = mid
            else:
                r = mid
    
    if nums[l] == target:
        return l
    if nums[r] == target:
        return r
    return -1
