def deleteDuplicatesUnsorted(self, head):
    dic = collections.defaultdict(int)
    cur = head
    while cur:
        dic[cur.val] += 1
        cur = cur.next
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while head:
        if dic[head.val] > 1:
            prev.next = head.next
        else:
            prev = prev.next          
        head = head.next
    return dummy.next
