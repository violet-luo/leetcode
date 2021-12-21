def addLists(self, l1, l2) -> list:
   dummy = cur = ListNode(0)
   carry = 0
   l1 = self.reverse(l1)
   l2 = self.reverse(l2)

   while l1 or l2 or carry:
     if l1:
         carry += l1.val
         l1 = l1.next
     if l2:
         carry += l2.val
         l2 = l2.next
     cur.next = ListNode(carry % 10) # carry的个位数
     cur = cur.next
     carry //= 10 # eg. s = 18, 18 // 10 = 1
   return self.reverse(dummy.next)

def reverse(self, head):
  prev, cur = None, head
  while cur:
      cur.next, prev, cur = prev, cur, cur.next
  return prev
