def divisibleTripletCount(self, nums: List[int], d: int) -> int:
    n = len(nums)
    two_sum = collections.defaultdict(list)
    cnt = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            remainder = (nums[i] + nums[j]) % d
            two_sum[remainder].append((i, j))

    for k in range(2, n):
        target = nums[k] % d
        two_sum_key = (d - target) % d

        if two_sum_key in two_sum:
            for (i, j) in two_sum[two_sum_key]:
                if j < k:
                    cnt += 1
    
    return cnt
