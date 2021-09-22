"""

Runtime: 36 ms, faster than 67.19% of Python3 online submissions for Partition List.
Memory Usage: 13.8 MB, less than 75.75% of Python3 online submissions for Partition List.

"""

def partition(self, head: ListNode, x: int) -> ListNode:
    # can't write as left = right = left_head = right_head
    left = left_head = ListNode(0) 
    right = right_head = ListNode(0) 

    if head is None:
        return None

    # can't write as while head and head.next or the last element will be omitted
    while head:
        if head.val < x:
            left.next = head
            left = left.next
        else:
            right.next = head
            right = right.next
        head = head.next

    right.next = None
    left.next = right_head.next
    return left_head.next
