def removeElements(self, head, val):
    if not head:
        return

    dummy = ListNode(0)
    dummy.next = head 
    cur = dummy
    
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next 
        else:
            cur = cur.next
            
    return dummy.next
