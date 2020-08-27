"""

Runtime: 24 ms, faster than 97.05% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 13.8 MB, less than 91.58% of Python3 online submissions for Reverse Linked List II.

code: https://leetcode.com/problems/reverse-linked-list-ii/discuss/30672/Python-one-pass-iterative-solution
drawing: https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)

"""

def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    pre, cur = dummy, head
    
    for _ in range(m - 1):
        cur, pre = cur.next, pre.next
    
    for _ in range(n - m):
        cur.next.next, pre.next, cur.next = pre.next, cur.next, cur.next.next

    return dummy.next
