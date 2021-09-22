def toLinkedList(self, nums):
    dummy = ListNode(0)
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next
