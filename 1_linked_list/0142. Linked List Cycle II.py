"""
1. Two Pointers

"""
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

###

def detectCycle(self, head):     
    if not head or not head.next:
        return None #不能是head #[1], -1会return[1]而不是-1
        
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if slow == fast:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next 
        return slow 
        
    return None


"""

2. Hash Map

Runtime: 96 ms, faster than 11.00% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.3 MB, less than 7.82% of Python3 online submissions for Linked List Cycle II.

"""

def detectCycle(self, head: ListNode) -> ListNode:
    res = set()

    while head:
        if head in res:
            return head
        else:
            res.add(head)
        head = head.next
    return None
