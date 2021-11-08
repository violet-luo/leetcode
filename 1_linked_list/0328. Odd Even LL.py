def oddEvenList(self, head):
    if head is None:
        return head

    odd = oddHead = ListNode(0)
    even = evenHead = ListNode(0)

    i = 1 # 这步是灵魂

    while head:
        if i % 2 == 1:
            odd.next = head
            odd = odd.next 
        else:
            even.next = head
            even = even.next
        i += 1
        head = head.next 

    even.next = None 
    odd.next = evenHead.next

    return oddHead.next
