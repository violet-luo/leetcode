"""
Reverse a singly linked list.

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Tutorial: https://www.youtube.com/watch?v=XDO6I8jxHtA
"""

# iterative
def reverse(self, head):
    cur, prev = head, None 
        
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev
    
    
# recursive
def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)
