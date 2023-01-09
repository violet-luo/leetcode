def computeax1rea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    # 没有重叠的情况
    if ay2 <= by1 or bx1 >= ax2 or ay1 >= by2 or bx2 <= ax1:
        return (ay2-ay1) * (ax2-ax1) + (by2-by1) * (bx2-bx1)
    
    # 重叠情况
    left = max(bx1, ax1)
    right = min(ax2, bx2)
    up = min(by2, ay2)
    down = max(by1, ay1)
    return (ay2-ay1) * (ax2-ax1) + (by2-by1) * (bx2-bx1) - (up-down) * (right-left)
