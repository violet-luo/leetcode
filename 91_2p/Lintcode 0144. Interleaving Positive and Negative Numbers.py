def rerange(self, A):
    neg_cnt = self.partition(A)
    pos_cnt = len(A) - neg_cnt
    # 如果负比正多，res以负打头，从第二个数开始交换
    left = 1 if neg_cnt > pos_cnt else 0
    # 如果正比负多，res以正打头，从第一个数开始交换
    right = len(A) - (2 if pos_cnt > neg_cnt else 1)
    self.interleave(A, left, right)
    
# 快分模板
def partition(self, A):
    left, right = 0, len(A) - 1
    while left <= right:
        while left <= right and A[left] < 0:
            left += 1
        while left <= right and A[right] > 0:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
    # 一般的快分return right, 但是这个结束时两个指针互换了位置
    return left
    

def interleave(self, A, left, right):
    while left < right:
        A[left], A[right] = A[right], A[left]
        # 间隔交换
        left, right = left + 2, right - 2
