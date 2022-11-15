def reverseList(self, head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next # 3,1,2 = 1,2,3
    return prev
