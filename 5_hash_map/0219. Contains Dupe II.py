def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    num_to_idx = collections.defaultdict(int)

    for i in range(len(nums)):
        if nums[i] in num_to_idx and abs(i - num_to_idx[nums[i]]) <= k:
            return True
        num_to_idx[nums[i]] = i
    
    return False
