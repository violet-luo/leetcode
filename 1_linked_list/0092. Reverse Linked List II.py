def reverseBetween(self, head, left, right):
    dummy = ListNode(0)
    dummy.next = head
    cur = head
    prev = dummy # 而不是None

    for _ in range(left - 1): # range(1) #0, 1
        cur, prev = cur.next, prev.next

    for _ in range(right - left): #range(2) # 2,3
        cur.next.next, prev.next, cur.next = prev.next, cur.next, cur.next.next

    return dummy.next
