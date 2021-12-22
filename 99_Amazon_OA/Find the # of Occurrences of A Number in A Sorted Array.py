def count(arr, target):
    n = len(arr)
    left = bisect_left(arr, target, 0, n)
    right = bisect_right(arr, target, left, n)  # use left as a lower bound
    return right - left
def bisect_left(a, x, lo, hi):
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo

def bisect_right(a, x, lo, hi):
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo
