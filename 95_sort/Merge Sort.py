def mergesort(self, arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2  # 将列表分成更小的两个列表

    left = self.mergesort(arr[:mid])
    right = self.mergesort(arr[mid:])
    return self.merge(left, right)

def merge(self, left, right):
    res = []
    i, j = 0, 0  

    # 对两个列表中的元素 两两对比。将最小的元素，放到res中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:] #遍历完了一个
    res += right[j:]
    return res
