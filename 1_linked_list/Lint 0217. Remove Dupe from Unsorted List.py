def removeDuplicates(self, head):
    if not head:
        return
    visited = set() # set and dict is O(1), list is O(n) exceeding time limit
    visited.add(head.val) # 要记得加入头元素
    
    cur = head
    while cur.next:
        if cur.next.val in visited:
            cur.next = cur.next.next
        else:
            visited.add(cur.next.val)
            cur = cur.next            

    return head
