def removeDuplicates(self, head):
    visited = set() # set and dict is O(1), list is O(n) exceeding time limit
    
    if not head:
        return head
    
    # 👁 一定要先加入头元素, 不然头元素可能会重复
    visited.add(head.val)
    
    cur = head
    while cur.next:
        if cur.next.val not in visited:
            visited.add(cur.next.val)
            cur = cur.next
        else:
            cur.next = cur.next.next

    return head
