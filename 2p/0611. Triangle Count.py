def triangleCount(self, S):
    if not S or len(S) < 3:
        return 0
    
    S.sort()
    ans = 0
    
    # 遍历最大边，在最大边的左边寻找两个小边
    # 从2开始找，保证前面至少有两个数
    for i in range(2, len(S)):
        ans += self.get_triangle_count(S, i)
    return ans
    
def get_triangle_count(self, ls, target_index):
    cnt = 0
    left = 0
    right = target_index - 1
    target_sum = ls[target_index]
    
    while left < right:
        # sum大于target,可以组成三角形
        if ls[left] + ls[right] > target_sum:
            # 一次求出多个可行解的个数
            # [1, 2, 2, 3, 3(大边)]
            # 当求出1和第四个3符合条件，right - left = 3 - 0 = 3 个可行解
            # 因为第二个2和第四个3 & 第三个2和第四个3 也符合条件
            cnt += right - left
            # 已经计入右指针所有可能的组合，右指针向中间移动
            right -= 1
        # sum小于target, 左指针向右移动，寻找更大sum
        else:
            left += 1
    return cnt
