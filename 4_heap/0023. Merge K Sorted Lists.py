def mergeKLists(self, lists):
    dummy = ListNode(0)
    cur = dummy
    heap = []

    for i in range(len(lists)): # 遍历3个链表 # i表明在第几个链表
        if lists[i]: # 遍历每个链表
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    while heap:
        val, idx = heapq.heappop(heap)
        cur.next = ListNode(val)
        cur = cur.next
        if lists[idx]:
            heapq.heappush(heap, (lists[idx].val, idx))
            lists[idx] = lists[idx].next

    return dummy.next
