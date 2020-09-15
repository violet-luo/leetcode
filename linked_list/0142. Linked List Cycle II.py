"""
1. Two Pointers

Runtime: 56 ms, faster than 54.96% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17 MB, less than 29.18% of Python3 online submissions for Linked List Cycle II.

"""

def getIntersect(self, head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None
    
def detectCycle(self, head: ListNode) -> ListNode:
    if head is None:
        return None
    
    intersect = self.getIntersect(head)
    if intersect is None:
        return None
    
    ptr1 = head
    ptr2 = intersect
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1


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
