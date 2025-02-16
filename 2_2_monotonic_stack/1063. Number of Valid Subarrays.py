def validSubarrays(self, nums: List[int]) -> int:
    stack = []
    count = 0

    for i, num in enumerate(nums):
		    # 当 stack 不为空，且 stack 顶部元素比 num 大
		    # 说明 stack[-1] 位置的元素 不能再向右扩展了
		    # 需要弹出 stack[-1] 并计算贡献的有效子数组
        while stack and nums[stack[-1]] > num:
            count += i - stack.pop()
        stack.append(i)
		
		# 3. 遍历完数组后，栈中剩余的索引 j，表示它们的有效子数组可以一直延伸到数组末尾 len(nums) - 1
    while stack:
        count += len(nums) - stack.pop()

    return count
