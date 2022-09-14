"""

Runtime: 136 ms, faster than 78.18% of Python3 online submissions for H-Index II.
Memory Usage: 20.5 MB, less than 64.84% of Python3 online submissions for H-Index II.

"""

def hIndex(self, citations: List[int]) -> int:
    # find the first citations[i] where citations[i] >= n - i
        # 若 citations[pivot] == n - pivot：则我们找到了想要的元素。
        # 若 citations[pivot] < n - pivot：由于我们想要的元素应该大于或等于 n - pivot，所以我们应该进一步搜索右边的子列表，即 citations[pivot + 1 : n]
        # 若 citations[pivot] > n - pivot：我们应该进一步搜索左边的子列表，即 citations[0 : pivot-1]
    n = len(citations)
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2
        if citations[mid] ==  n - mid:
            return n - mid
        elif citations[mid] < n - mid:
            left = mid + 1
        else:
            right = mid - 1

    return n - left
