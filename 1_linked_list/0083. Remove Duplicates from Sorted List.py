"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
Input: 1->1->2
Output: 1->2


Runtime: 44 ms, faster than 44.57% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14 MB, less than 6.45% of Python3 online submissions for Remove Duplicates from Sorted List.
"""

def deleteDuplicates(self, head):
    if not head:
        return head
    cur = head
    while cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
