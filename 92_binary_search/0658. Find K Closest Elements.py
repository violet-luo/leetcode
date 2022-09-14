def kClosestNumbers(self, A, target, k):
    right = self.findUpperClosest(A, target)
    left = right - 1
    
    # 两根指针从中间往两边扩展，依次找到最接近的k个数
    results = []
    for _ in range(k): #我不需要用到_这个循环变量
        # 如果左边更接近，选左边
        if self.isLeftCloser(A, target, left, right):
            results.append(A[left])
            left -= 1
        else:
            results.append(A[right])
            right += 1
    return results

def isLeftCloser(self, A, target, left, right):
    # 如果左边已经耗尽，返回false
    if left < 0:
        return False

    # 如果右边已经耗尽，返回true
    if right >= len(A):
        return True

    # 为什么有等号？如果左右距离相等，选左边
    return target - A[left] <= A[right] - target

# find first target
# 找到最左边的 >= target的元素
def findUpperClosest(self, A, target):
    start, end = 0, len(A) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        # 如果mid >= target, mid符合条件向左边去寻找
        # 更靠左的符合条件的元素，丢掉右边
        if A[mid] >= target:
            end = mid
        # 如果mid < target, >= target的元素在右边，丢掉左边
        else:
            start = mid

    # 因为需要找最左数，所以这里需要先判断start
    if A[start] >= target:
        return start
    # 如果end不行，再判断start
    if A[end] >= target:
        return end

    # 找不到的情况
    return len(A)
