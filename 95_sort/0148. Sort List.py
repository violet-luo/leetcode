def sortList(self, head):
    if not head or not head.next:
        return head
    #把链表分成左右两半    
    mid = self.find_mid(head)
    left = head
    right = mid.next
    mid.next = None
    
    sorted_left = self.sortList(left)
    sorted_right = self.sortList(right)
    
    return self.merge(sorted_left, sorted_right)
    
def find_mid(self, head):
    if not head or not head.next:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
def merge(self, l1, l2): #参见Lintcode#165 Merge Two Sorted Lists
    if not l1: return l2
    if not l2: return l1
    dummy = ListNode(0)
    cur = dummy

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            cur = cur.next
            l1 = l1.next
        else:
            cur.next = l2
            cur = cur.next
            l2 = l2.next
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2
        
    return dummy.next
