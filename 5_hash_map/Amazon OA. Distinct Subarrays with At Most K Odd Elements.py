def distinct_subarrays(nums, k):
    visited = set()
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            oddnum = 0
        else:
            oddnum = 1
        
        for j in range(i+1, len(nums)+1):
            if tuple(nums[i:j]) not in visited:
                visited.add(tuple(nums[i:j]))
            if j < len(nums):
                if nums[j] % 2 == 1:
                    oddnum += 1
                    if oddnum > k:
                        break
            
    return len(visited)
