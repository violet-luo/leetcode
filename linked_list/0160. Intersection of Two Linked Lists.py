"""

Runtime: 240 ms, faster than 16.59% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.1 MB, less than 47.46% of Python3 online submissions for Intersection of Two Linked Lists.

"""

def getIntersectionNode(self, L1: ListNode, L2: ListNode) -> ListNode:
    if not headA or not headB:
        return None
    
    pA, pB = headA, headB
    
    while pA is not pB: #preferred than pA != pB b/c we care more than the values
        pA = headB if pA is None else pA.next #TLE if pA = pA.next if pA else headA
        pB = headA if pB is None else pB.next
    return pA
