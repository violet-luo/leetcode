def rotateRight(self, head, k):
    if not head:
        return
    slow = fast = head
    length = 1
    
    #  1. 得到链表长度
    while fast and fast.next:
        fast = fast.next
        length += 1
    
    fast.next = head # 环形链表
    k %= length # k可能比len长
    
    # slow走到rotate之前的一个元素
    for _ in range(length - k - 1):
        slow = slow.next
         
    res = slow.next # 4
    slow.next = None # 3.next = None
    return res
