def minTaps(self, n: int, ranges: List[int]) -> int:
    # 1. 得到水龙头的灌溉区间
    intervals = []
    for i, r in enumerate(ranges):
        left, right = max(0, i - r), min(n, i + r)
        intervals.append((left, right)) # [(0, 3), (0, 5), (1, 3), (2, 4), (4, 4), (5, 5)]

    # 2. 按起点排序
    intervals.sort()

    # 3. 找到所有起点 ≤ curr_end 的水龙头，选择最远的水龙头
    taps = 0
    curr_end, max_reach, i = 0, 0, 0

    while curr_end < n:
        while i <= n and intervals[i][0] <= curr_end:
            max_reach = max(max_reach, intervals[i][1])
            i += 1

        if max_reach <= curr_end:
            return -1  # If we can't extend coverage, return -1

        taps += 1
        curr_end = max_reach  # Extend the watering range

    return taps
