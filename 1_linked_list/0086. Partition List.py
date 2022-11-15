def partition(self, head, x):
    if not head:
        return 
    left = left_dummy = ListNode(0)
    right = right_dummy = ListNode(0)

    # can't write as while head and head.next or the last element will be omitted
    while head:
        if head.val < x:
            left.next = head
            left = left.next
        else:
            right.next = head
            right = right.next
        head = head.next
    
    right.next = None
    left.next = right_dummy.next
    return left_dummy.next
