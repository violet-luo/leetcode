def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    # 1. 在每一个结点后复制一个结点
    # 7→7′→13→13′→11→11′
    cur = head
    while cur:
        cur.next = Node(cur.val, cur.next)
        cur = cur.next.next
    
    # 2. 新结点拷贝老结点的random pointer
    cur = head
    while cur:
        if cur.random: # 只遍历旧结点
            cur.next.random = cur.random.next # 新结点拷贝老结点的random pointer, 7‘.random -> 11'
        cur = cur.next.next
    
    # 3. 断开链表
    cur = head.next
    while cur.next:
        cur.next = cur.next.next
        cur = cur.next
        
    return head.next
