def containsNearbyDuplicate(self, nums, k):
    dic = {}

    for i in range(len(nums)):
        if nums[i] in dic and abs(i - dic[nums[i]]) <= k:
            return True
        dic[nums[i]] = i
    return False
