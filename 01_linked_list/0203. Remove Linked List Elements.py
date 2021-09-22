"""

Runtime: 76 ms, faster than 72.26% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 16.9 MB, less than 51.73% of Python3 online submissions for Remove Linked List Elements.

"""

def removeElements(self, head: ListNode, val: int) -> ListNode:
    dummy_head = ListNode(-1)
    dummy_head.next = head 
    current_node = dummy_head 

    while current_node.next != None:
        if current_node.next.val == val:
            current_node.next = current_node.next.next 
        else:
            current_node = current_node.next

    return dummy_head.next
