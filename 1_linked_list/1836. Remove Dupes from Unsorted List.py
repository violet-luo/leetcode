def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
    dic = collections.defaultdict(int)
    cur = head
    while cur:
        dic[cur.val] += 1
        cur = cur.next
    
    dummy = ListNode(0)
    dummy.next = head
    cur = dummy

    while cur.next:
        if dic[cur.next.val] > 1:
            cur.next = cur.next.next  # Skip the duplicate
        else:
            cur = cur.next  # Move to the next node
    
    return dummy.next
        
###

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
