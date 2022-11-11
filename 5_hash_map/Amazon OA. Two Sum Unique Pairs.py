def two_sum_unique_pairs(nums, target):
    res = set()
    complements = set()
    
    for num in nums:
        if num not in complements:
            complements.add(target - num)
        else:
            res.add((item, target - num))
    return len(res)

def two_sum_unique_pairs(nums, target):
  res, pairs = set(), set()

  for num in nums:
    complement = target - num
    if num > complment:
        pair = (complement, num)
    else:
        pair = (num, complement)

    if pair not in pairs:
        pairs.add(pair) # 见了一次
    else: 
        res.add(pair) # 见了第二次

  return len(res)
