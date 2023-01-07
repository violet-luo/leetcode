class TwoSum:
    def __init__(self):
        self.nums = {}

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value: int) -> bool:
        for num in self.nums:
            if value - num in self.nums and (value - num != num or self.count[num] > 1):
                return True
        return False
