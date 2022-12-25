def findDuplicate(self, nums):
    slow = nums[0]
    fast = nums[slow]

    # 1. 慢指针走一步，快指针走两步，直到相遇
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    # 2. 快指针归零，慢指针和快指针各走一步，相遇点为环入口 
    fast = 0
    while fast != slow:
        fast = nums[fast]
        slow = nums[slow]
    
    return slow
