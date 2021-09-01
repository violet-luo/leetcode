def twoSum(self, numbers, target):
     # nlogn
    numbers.sort()
    
    # n
    left, right = 0, len(numbers) - 1
    while left < right：
        if numbers[left] + numbers[right] > target:
            right-= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            return numbers[left], numbers[right]
            
    return [-1, 1]
