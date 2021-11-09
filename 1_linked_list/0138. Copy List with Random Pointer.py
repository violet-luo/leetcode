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
