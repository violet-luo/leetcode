def toLinkedList(self, nums):
    dummy = ListNode(0)
    cur = dummy
    
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next
