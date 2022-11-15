def removeNthFromEnd(self, head):
    if not head or not head.next:
       return #[1] return [1] instead of []

    dummy = ListNode(0)
    dummy.next = head
    cur = dummy

    while cur.next and cur.next.next:
        fst, sec = cur.next, cur.next.next

        cur.next = sec
        fst.next = sec.next
        sec.next = fst

        cur = cur.next.next 

    return dummy.next
