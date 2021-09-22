"""

Runtime: 100 ms, faster than 64.78% of Python3 online submissions for Reorder List.
Memory Usage: 23.1 MB, less than 83.81% of Python3 online submissions for Reorder List.

"""

def reorderList(self, head: ListNode) -> None:
    if head is None:
        return None

    slow = fast = head

    # 1. find the mid point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. reverse the second half in-place
    prev, slow.next, slow = None, None, slow.next
    while slow:
        prev, prev.next, slow = slow, prev, slow.next

    # 3. merge lists
    slow = head
    while prev:
        slow.next, slow = prev, slow.next
        prev.next, prev = slow, prev.next
