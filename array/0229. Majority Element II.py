"""

1. Extra space
Runtime: 104 ms, faster than 96.07% of Python3 online submissions for Majority Element II.
Memory Usage: 15.1 MB, less than 54.85% of Python3 online submissions for Majority Element II.

"""

def majorityElement(self, nums: List[int]) -> List[int]:
    ans=[]
    for num in list(set(nums)):
        if nums.count(num) > len(nums)/3:
            ans.append(num)
    return list(set(ans))
   
   
"""

2. No extra space
Runtime: 108 ms, faster than 87.91% of Python3 online submissions for Majority Element II.
Memory Usage: 15.4 MB, less than 12.88% of Python3 online submissions for Majority Element II.

"""

def majorityElement(self, nums: List[int]) -> List[int]:
    if not nums:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, 0, 1
    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = n, 1
        elif count2 == 0:
            candidate2, count2 = n, 1
        else:
            count1, count2 = count1 - 1, count2 - 1
    return [n for n in (candidate1, candidate2)
                    if nums.count(n) > len(nums) // 3]
