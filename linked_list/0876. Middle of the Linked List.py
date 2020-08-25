"""

Runtime: 36 ms, faster than 41.16% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14 MB, less than 11.75% of Python3 online submissions for Middle of the Linked List.

"""

def middleNode(self, head: ListNode) -> ListNode:
    slow = fast = head

    if head is None:
        return None

    # if len == odd, fast will point to null if not add fast is not None
    while fast is not None and fast.next is not None: 
        slow = slow.next
        fast = fast.next.next 

    return slow
