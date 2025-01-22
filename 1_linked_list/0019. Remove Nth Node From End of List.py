def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    cur = head

    length = 0
    while cur:
        length += 1
        cur = cur.next

    cur = dummy
    for _ in range(length - n):
        cur = cur.next
    
    cur.next = cur.next.next
    return dummy.next
        
###


def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        fast = slow = dummy 
        
        # _ is not used in the loop can be any letter
        for _ in range(n): 
            # fast指向链表第n个元素
            fast = fast.next #
            
        # 直至fast=Null，此时slow指向倒数第n个元素。
        while fast.next is not None:
            fast = fast.next 
            slow = slow.next
        
        # skip the nth node
        slow.next = slow.next.next
        
        return dummy.next
