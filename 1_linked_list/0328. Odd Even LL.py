def oddEvenList(self, head):
    if not head:
        return
    odd = odd_dummy = ListNode(0)
    even = even_dummy = ListNode(0)

    i = 1 # 因为是索引为奇数所以不能直接 head.val % 2 == 1

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
    odd.next = even_dummy.next
    return odd_dummy.next
