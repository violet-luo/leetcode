"""

Runtime: 36 ms, faster than 95.31% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 13.8 MB, less than 78.35% of Python3 online submissions for Remove Duplicates from Sorted List II.

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28336/Python-in-place-solution-with-dummy-head-node.

"""

def deleteDuplicates(self, head: ListNode) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    
    # set up pre and cur pointers
    pre, cur = dummy, head
    
    while cur:
        if cur.next and cur.val == cur.next.val:
            # loop till cur point hits the last dupe
            while cur and cur.next and cur.val == cur.next.val:
                cur = cur.next
            # pre points to the node after the last dupe
            pre.next = cur.next
        else:
            # anyways pre has to move forward
            pre = pre.next
        # anyways cur has to move forward
        cur = cur.next
    
    return dummy.next
