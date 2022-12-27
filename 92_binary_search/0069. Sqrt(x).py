def mySqrt(self, x):
    l, r = 0, x

    while l + 1 < r:
        mid = (l + r) // 2
        if mid * mid < x:
            l = mid
        elif mid * mid > x:
            r = mid
        else:
            return mid 
    
    if r * r <= x: #不加等号 x = 1时会return0
        return r 
    return l

###

def mySqrt(self, x: int) -> int:
    l, r, ans = 0, x, -1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans
