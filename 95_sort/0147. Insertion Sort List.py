def insertionSortList(self, head):
    if not head:
        return head
    dummy = ListNode(0, head)
    cur = head

    while cur.next:
        if cur.val <= cur.next.val:
            cur = cur.next
        else:
            start = dummy #从头开始寻找插入位置，最终在start的后面
            node_to_insert = cur.next
            while start.next.val <= node_to_insert.val: #当start的next的值比待排的大
                start = start.next

            cur.next = node_to_insert.next
            node_to_insert.next = start.next
            start.next = node_to_insert
