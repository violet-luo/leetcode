def productExceptSelf(nums): #[1,2,3,4]
    p = 1
    n = len(nums)
    res = []
    
    # 当前数左边的乘积
    for i in range(0, n): #[1,1,2,6]
        res.append(p)
        p *= nums[i]

    # 当前数右边的乘积
    p = 1
    for i in range(n - 1, -1, -1): #[24,12,8,6]
        res[i] = res[i] * p
        p *= nums[i]
    return res
