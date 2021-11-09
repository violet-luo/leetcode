"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
   def copyRandomList(self, head):
      if not head:
         return None
      #  mapping the node to new node
      mapping = {}
      curr = head
      while curr:
         mapping[curr] = RandomListNode(curr.label)
         curr = curr.next

      #  copy the next and ramdon pointer
      for node in mapping:
         if node.next:
             mapping[node].next = mapping[node.next]
         if node.random:
             mapping[node].random = mapping[node.random]
             
      return mapping[head]

def copyRandomList1(self, head):
  if not head:
      return 
  
  # 1. 在每一个结点后复制一个没有指向的结点
  cur = head
  while cur:
      nxt = cur.next
      cur.next = RandomListNode(cur.label)
      cur.next.next = nxt
      cur = nxt
  
  # 2. 新结点拷贝老结点的random pointer
  cur = head
  while cur: 
      if cur.random: # 只遍历旧结点
          cur.next.random = cur.random.next # 新结点拷贝老结点的random pointer
      cur = cur.next.next
  
  # 3. 断开链表
  second = cur = head.next
  while cur.next:
      head.next = cur.next
      head = head.next
      cur.next = head.next
      cur = cur.next
  head.next = None
  return second
