def isPerfectSquare(num):
    l, r = 0, num

    while l + 1 < r:
        mid = (l + r) // 2
        if mid * mid < num:
            l = mid
        elif mid * mid > num:
            r = mid
        else:
            return True
    
    if l * l == num or r * r == num:
        return True
    return False

###

def isPerfectSquare(num):
    l, r = 0, num
    
    # 如果没有等号, l 和 r 不会相交, 最后一次一定是 m 收敛到 l, 而取不到r
    while l <= r: 
        mid = (l + r) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            l = mid + 1
        else:
            r = mid - 1
        
    return False
