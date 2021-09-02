def threeSum(self, numbers):
    results = []
    
    if not numbers or len(numbers) < 3:
        return results
        
    numbers.sort()
    
    length = len(numbers)
    # 遍历三元组中的最小数
    for i in range(0, length - 2):
        # 经典去重套路
        # 如果当前元素和左边元素一样，跳过
        if i > 0 and numbers[i] == numbers[i-1]:
            continue
        # abc, a为i，在 i+1 到 len-1 间寻找 bc    
        left = i + 1
        right = length - 1
        target = -numbers[i]
        # 用经典的two sum
        self.find_two_sum(numbers, left, right, target, results)
    return results

# 带有去重逻辑的相向双指针Two Sum
# [-7, 2, 2, 3, 4, 5, 5]
def find_two_sum(self, numbers, left, right, target, results):
    while left < right:
        # [2........5]
        if numbers[left] + numbers[right] == target:
            results.append([-target, numbers[left], numbers[right]])
            # 两边同时移动
            right -= 1
            left += 1
            # 如果左指针当前数字和左边数字相同，左指针向中间移动，跳过重复
            # [3, 4]
            while left < right and numbers[left] == numbers[left - 1]:
                left += 1
            while left < right and numbers[right] == numbers[right + 1]:
                right -= 1
        # 当前 sum 小于 target, 右移左指针，去找更大的sum
        elif numbers[left] + numbers[right] > target:
            right -= 1
        # 当前 sum 大于 target, 左移右指针，去找更小的sum
        else:
            left += 1
