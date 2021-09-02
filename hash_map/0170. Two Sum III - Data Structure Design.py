"""
1. 使用哈希表的方法是最快的

add: O(1)
find: O(n)
"""

def __init__(self):
    # key是数字，value是数字出现的次数
    self.count = {}
        
# Add the number to an internal data structure.
# @param number {int}
# @return nothing
# 数字出现次数+1，如果这个数字第一次出现，则之前出现的次数为0
def add(self, number):
    if number in self.count:
        self.count[number] += 1
    else:
        self.count[number] = 1

# Find if there exists any pair of numbers which sum is equal to the value.
# @param value {int}
# @return true if can be found or false
def find(self, value):
    # 遍历map中所有的key
    for num1 in self.count:
        # 寻找跟num1匹配的num2
        num2 = value - num1
        num2Cnt = 2 if (num1 == num2) else 1
        # 如果找到，返回True.如果找不到，则出现次数为0
        if self.num_to_cnt_map.get(num2, 0) >= num2Cnt:
            return True
    return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)


"""
2. 排序数组+双指针的算法会超时，但是大家可以看看是怎么写的

add: O(n)
find: O(n)
"""

def __init__(self):
   # list装升序数据，因为Two Sum需要在有序数列中寻找
    self.nums = []
    
def add(self, number):
    self.nums.append(number)
    index = len(self.nums) - 1
    # 按照插入排序的方法， 加入新数字，保持nums升序
    # 每次将数组最后一个元素作为插入元素，与它前面有序（已排好序）的数组元素依次进行比较
    # 如果没有在正确的位置，交换两元素，继续下一轮比较
    # 如果在正确的位置，结束
    # 为什么要确保 index > 0 ? 因为需要获得数组中(index - 1)位置的数字
    while index > 0 and self.nums[index-1] > self.nums[index]:
        # 在list中，交换(index-1)和index对应的值
        self.nums[index-1], self.nums[index] = self.nums[index], self.nums[index-1]
        index -= 1
   
# 经典two sum, 在排序树组中用相向双指针寻找和为target的一对数字      
def find(self, targetValue):
    left, right = 0, len(self.nums) - 1
    whiel left < right:
        two_sum = self.nums[left] + self.nums[right]
        if two_sum < targetValue:
            left += 1
        elif two_sum > targetValue:
            right -= 1
        else:
            return True
    return False
