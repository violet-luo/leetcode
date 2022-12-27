def search(self, nums: List[int], target: int) -> bool:
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        # 比33多了去重逻辑
        while nums[l] == nums[l+1] and l + 1 < r:
            l += 1
        while nums[r] == nums[r-1] and l + 1 < r:
            r -= 1
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            if nums[l] <= target <= nums[mid]:
                r = mid
            else:
                l = mid
        else:
            if nums[mid] <= target <= nums[r]:
                l = mid
            else:
                r = mid
    if nums[l] == target:
        return True
    if nums[r] == target:
        return True
    return False
