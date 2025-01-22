 def isPalindrome(self, head: Optional[ListNode]) -> bool:
     slow = fast = head

     # 1. Middle of the LL
     # slwo指向第二部分链表的起点
     # [1,2,2,1] slow = 第二个2
     # [1,2,3,2,1] slow = 3
     while fast and fast.next:
         slow = slow.next 
         fast = fast.next.next
     
     # 2. Reverse 2nd part LL
     prev = None
     cur = slow
     while cur:
         tmp = cur.next
         cur.next = prev
         prev = cur
         cur = tmp
     
     while prev:
         if head.val != prev.val:
             return False
         head, prev = head.next, prev.next 
     return True

###

def isPalindrome(self, head: ListNode) -> bool:
   if head is None:
        return True # 注意这题不是return None 或者可以不用加这两行
   
   slow = fast = head
    
   # 1. 先找到中点
   while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

   # 2. 把后半段倒过来
   prev = None # 这里和上题不同
   while slow:
      prev, prev.next, slow = slow, prev, slow.next

   # 3. 前后比较
   while prev:
      if head.val != prev.val:
         return False
      head, prev = head.next, prev.next 
   return True
