def getIntersectionNode(self, headA, headB):
    if not headA or not headB:
        return None
    
    a, b = headA, headB
    
    while a != b:
	      # 当 a 到达链表末尾时，将它重新定位到链表 headB 的头部
        a = headB if a is None else a.next
        b = headA if b is None else b.next
    return a # 当 a == b 时，返回当前节点（可能是交点，也可能是 None）
