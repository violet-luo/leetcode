"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
Input: 1->1->2
Output: 1->2


Runtime: 44 ms, faster than 44.57% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14 MB, less than 6.45% of Python3 online submissions for Remove Duplicates from Sorted List.
"""


def deleteDuplicates(head):
    """
    :type head: listNode
    :rtype: listNode
    """
    current = head

    while current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
