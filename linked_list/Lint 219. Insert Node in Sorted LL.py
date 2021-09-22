def insertNode(self, head, val):
      dummy = ListNode(0, head)
      p = dummy
      while p.next and p.next.val < val:
          p = p.next
      node = ListNode(val, p.next)
      p.next = node
      return dummy.next
