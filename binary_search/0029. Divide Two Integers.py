"""

Runtime: 24 ms, faster than 97.19% of Python3 online submissions for Divide Two Integers.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Divide Two Integers.

"""

def divide(self, dividend: int, divisor: int) -> int:
    min_int, max_int = -2147483648, 2147483647 # [-2^31, 2^31-1]
    flag = 1                                   # 存储正负号，并将分子分母转化为正数
    if dividend < 0:
        flag, dividend = -flag, -dividend
    if divisor < 0:
        flag, divisor = -flag, -divisor

    res = 0
    while dividend >= divisor:
        cur = divisor
        multiple = 1
        while cur + cur < dividend:             # 用加法求出保证divisor * multiple <= dividend的最大multiple
            cur += cur                          # 即cur分别乘以1, 2, 4, 8, 16...2^n，即二进制搜索
            multiple += multiple
        dividend -= cur
        res += multiple

    res = res if flag > 0 else -res             # 恢复正负号

    if res < min_int:                           # 根据是否溢出返回结果
        return min_int
    elif min_int <= res <= max_int:
        return res
    else:
        return max_int
