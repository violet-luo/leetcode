def deleteDuplicates(self, head):
    dummy = ListNode(0)
    dummy.next = head
    cur = dummy 

    while cur and cur.next and cur.next.next:
        if cur.next.val == cur.next.next.val:
            node = cur.next.next # node = cur.next也可以
            # 要run node = node.next 一定要 check while node 不然会 runtime error
            # cur.next.val是重复数值的第一个数，loop到重复数值的后一个数
            while node and node.val == cur.next.val:
                node = node.next
            cur.next = node
        else:
            cur = cur.next

    return dummy.next
