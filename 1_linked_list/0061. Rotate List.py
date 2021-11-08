def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if head is None:
        return None

    slow = fast = head
    length = 1
    
    # fast走到队尾
    while fast and fast.next:
        fast = fast.next
        length += 1
    
    fast.next = head # 环形链表
    k %= length # k可能比len长
    
    # slow走到rotate之前的一个元素
    for _ in range(length - k - 1):
        slow = slow.next
         
    ans = slow.next
    slow.next = None # 斩断 slow 和 ans 的指向
    return ans
