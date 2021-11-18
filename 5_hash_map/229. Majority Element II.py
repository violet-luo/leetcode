def majorityNumber(self, nums):
    key1, counter1 = None, 0
    key2, counter2 = None, 0
    for num in nums:
        if key1 == num:
            counter1 += 1
        elif key2 == num:
            counter2 += 1
        elif counter1 == 0:
            key1 = num
            counter1 += 1
        elif counter2 == 0:
            key2 = num
            counter2 += 1
        else:
            counter1 -= 1
            counter2 -= 1

    counter1, counter2 = 0, 0
    for num in nums:
        if num == key1:
            counter1 += 1
        if num == key2:
            counter2 += 1

    return key1 if counter1 > counter2 else key2
  
def majorityNumber(self, nums):
    table = {}
    for i, num in enumerate(nums):
        if num not in table:
            table[num] = 1
        else:
            table[num] += 1
    
    for key, value in table.items():
        if value > len(nums) // 3:
            return key
