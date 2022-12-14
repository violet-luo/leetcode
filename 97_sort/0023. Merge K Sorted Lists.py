def mergeKLists(self, lists):
    if lists == []:
        return None
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = self.mergeKLists(lists[:mid])
    right = self.mergeKLists(lists[mid:])
    return self.merge(left, right)
    
def merge(self, left, right):
    dummy = ListNode(None)
    h = dummy

    while left and right:
        if left.val < right.val:
            h.next = left
            left = left.next
        else:
            h.next = right
            right = right.next
        h = h.next
        
    if left:
        h.next = left
    if right:
        h.next = right
    return dummy.next
