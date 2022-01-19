def insertNode(self, head, val):
    dummy = ListNode(0)
    dummy.next = head
    cur = dummy

    # 行进到插入点
    while cur.next and cur.next.val < val:
        cur = cur.next
    # 先定义node, 再插入
    node = ListNode(val, cur.next)
    cur.next = node
    return dummy.next #head有可能更改，所以插入dummy.next
