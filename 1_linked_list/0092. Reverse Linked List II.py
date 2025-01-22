def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    cur = head
    prev = dummy

    # prev走到换的left前, cur走到left
    # prev在1，cur在2
    for _ in range(left - 1):
        prev = prev.next
        cur = cur.next
    leftmost = prev
    rightmost = cur

    # 206. reverse LL
    prev = None
    for _ in range(right - left + 1): # three nodes, swap three times
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
        
    leftmost.next = prev
    rightmost.next = cur
    
    return dummy.next

###

def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    cur = head
    prev = dummy

    # prev走到换的left前, cur走到left
    # prev在1，cur在2
    for _ in range(left - 1):
        prev = prev.next
        cur = cur.next
    
    for _ in range(right - left): # range(2), swap twice
        # First swap
        # prev = 1, cur = 2
        # 1 -> 3 -> 2 -> 4 -> 5
        # Second swap 
        # prev = 1, cur = 2
        # 1 -> 4 -> 3 -> 2 -> 5
        temp = cur.next # 3
        cur.next = temp.next # 2 -> 4
        temp.next = prev.next # 3 -> 2
        prev.next = temp # 1 -> 3

    return dummy.next

###

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
