"""
Runtime: 36 ms, faster than 68.12% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.8 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
"""

def mergeTwolists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # define the head of the linked list
    # current keeps moving so we add dummy to keep the pointer at list head to print out the whole list
    
    current = dummy = ListNode(0)
    
    while l1 and l2:
    # first insert the smaller value from the two lists
        
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
            
        current = current.next
    
    # return the non None list
    # if one of the lists is at the end(means None), then the other one will append to the result directly.
    current.next = l1 or l2
    
    return dummy.next
