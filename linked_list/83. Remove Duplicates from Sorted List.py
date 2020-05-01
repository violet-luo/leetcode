"""
Runtime: 44 ms, faster than 44.57% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14 MB, less than 6.45% of Python3 online submissions for Remove Duplicates from Sorted List.
"""


def deleteDuplicates(head):
    """
    :type head: listNode
    :rtype: listNode
    """
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
