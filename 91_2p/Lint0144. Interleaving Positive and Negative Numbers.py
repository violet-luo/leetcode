def rerange(self, A):
    neg_cnt = self.partition(A)
    pos_cnt = len(A) - neg_cnt
    # 如果负比正多，res以负打头，从第二个数开始交换
    l = 1 if neg_cnt > pos_cnt else 0
    # 如果正比负多，res以正打头，从第一个数开始交换
    r = len(A) - (2 if pos_cnt > neg_cnt else 1)
    self.interleave(A, l, r)
    
# partition array 模板
def partition(self, A):
    l, r = 0, len(A) - 1
    while l <= r:
        while l <= r and A[l] < 0:
            l += 1
        while l <= r and A[r] > 0:
            r -= 1
        if l <= r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1
    # 一般的快分return r, 但是这个结束时两个指针互换了位置
    return l
    
def interleave(self, A, l, r):
    while l < r:
        A[l], A[r] = A[r], A[l]
        # 间隔交换
        l, r = l + 2, r - 2
