def findNode(self, head, val):
    while head:
        if head.val == val:
            return head
        else:
            head = head.next
    return None
