def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    dummy = ListNode(0, head)
    cur = head

    while cur.next: # 循环里需要cur.next.val
		    # 1. 找一个比前一个数小的数，cur为大数，cur.next为小数
		    # cur = 5, cur.next = 2
        if cur.val <= cur.next.val: 
            cur = cur.next
        else:
            insertion_point = dummy
            node_to_insert = cur.next
            # 2. 找insertion_point < node < insertion_point.next
            # 一直走到insertion_point.next的值比待排的大
            # insertion_point = 1, insertion_point.next = 3
            while insertion_point.next.val <= node_to_insert.val: 
                insertion_point = insertion_point.next
						
						# 3. 把node插入insertion和next之间
            cur.next = node_to_insert.next # 把待插入节点从链表中移除
            node_to_insert.next = insertion_point.next # 插入节点的后继设为 start.next
            insertion_point.next = node_to_insert # 完成插入，将 start 的 next 指向插入节点

    return dummy.next
