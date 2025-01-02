class TwoSum:

    def __init__(self):
        self.dic = {} # 不能用defaultdict

    def add(self, number: int) -> None:
        if number in self.dic:
            self.dic[number] += 1
        else:
            self.dic[number] = 1

    def find(self, value: int) -> bool:
        for num in self.dic:
            complement = value - num
            if complement in self.dic:
                # Special case: if the number is the same, we need at least two occurrences of it
                if complement != num or self.dic[num] > 1:
                    return True
        return False
