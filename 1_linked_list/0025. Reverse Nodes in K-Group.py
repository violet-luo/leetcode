def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    cur = head
    
    length = 0
    while cur:
        length += 1
        cur = cur.next
    
    prev = dummy
    cur = head
    reversed_times = length // k
    for i in range(reversed_times):
        before_start = prev
        start = cur
        for j in range(k):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        before_start.next = prev
        start.next = cur
        prev = start

    return dummy.next
