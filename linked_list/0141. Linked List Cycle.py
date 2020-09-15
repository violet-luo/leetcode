"""

1. Two Pointers

Runtime: 52 ms, faster than 58.72% of Python3 online submissions for Linked List Cycle.
Memory Usage: 16.8 MB, less than 70.46% of Python3 online submissions for Linked List Cycle.

"""

def hasCycle(self, head: ListNode) -> bool:
    if not head or not head.next:
        return None

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        else:
            slow = slow.next
            fast = fast.next.next
    return False
    
"""

2. Hash Map

Runtime: 44 ms, faster than 92.12% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.3 MB, less than 5.30% of Python3 online submissions for Linked List Cycle.

"""

def hasCycle(self, head: ListNode) -> bool:
    res = set()

    if head in set():
        return True

    while head:
        if head in res:
            return True
        else:
            res.add(head)
        head = head.next
    return False
