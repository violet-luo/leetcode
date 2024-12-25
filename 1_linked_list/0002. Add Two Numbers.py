def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    head = dummy
    carry = 0
    
    while l1 and l2:
        digit = (l1.val + l2.val + carry) % 10
        carry = (l1.val + l2.val + carry) // 10
        head.next = ListNode(digit)
        head = head.next
        l1 = l1.next
        l2 = l2.next
    
    while l1:
        digit = (l1.val + carry) % 10
        carry = (l1.val + carry) // 10
        head.next = ListNode(digit)
        head = head.next
        l1 = l1.next
    
    while l2:
        digit = (l2.val + carry) % 10
        carry = (l2.val + carry) // 10
        head.next = ListNode(digit)
        head = head.next
        l2 = l2.next
    
    if carry > 0:
        head.next = ListNode(carry)
    return dummy.next
        
###

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next
