"""
1. 使用哈希表的方法是最快的

add: O(1)
find: O(n)
"""

def __init__(self):
    # initialize your data structure here
    self.count = {}
        
    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        for num in self.count:
            if value - num in self.count and (value - num != num or self.count[num] > 1):
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
        self.nums = []
        
def add(self, number):
    self.nums.append(number)
    index = len(self.nums) - 1
    while index > 0 and self.nums[index - 1] > self.nums[index]:
        temp = self.nums[index - 1]
        self.nums[index - 1] = self.nums[index]
        self.nums[index] = temp
        index -= 1

def find(self, value):
    left, right = 0, len(self.nums) - 1
    while left < right:
        two_sum = self.nums[left] + self.nums[right]
        if two_sum < value:
            left += 1
        elif two_sum > value:
            right -= 1
        else:
            return True
    return False
