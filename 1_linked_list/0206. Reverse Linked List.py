def reverse(self, head):
	  prev, cur = None, head
	  while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
	  return prev
