def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    res = []
    q = collections.deque()

    for i in range(len(nums)):
        # 1. 入
        while q and nums[q[-1]] < nums[i]:
            q.pop()
        q.append(i)

        # 2. 出
        # 窗口的右边界是i, 左边界是i - k + 1, 如果队头索引q[0]小于左边界，说明它已经不在窗口中了，弹出
        if q[0] < i - k + 1
            q.popleft()

        # 3. 从滑动窗口>=k时开始记录答案
        if i >= k - 1: 
            res.append(nums[q[0]])

    return res
