"""

Runtime: 28 ms, faster than 88.44% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.9 MB, less than 29.99% of Python3 online submissions for Swap Nodes in Pairs.

https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode

"""

def swapPairs(self, head: ListNode) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    cur = dummy #dummy will not change and can be returned

    if head is None: # and head.next is None: head does not have attribute None
        return 
    elif head and head.next is None:
        return head 
    else:
        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next
        return dummy.next
