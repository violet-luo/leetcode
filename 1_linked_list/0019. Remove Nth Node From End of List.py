"""

Challenge is to do it without getting the length of the linked list
创建两个指针，slow指向表头、fast指向链表第n个元素
循环后移n次，直至fast=Null，此时slow指向倒数第n个元素

Runtime: 56 ms, faster than 16.79% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.9 MB, less than 26.61% of Python3 online submissions for Remove Nth Node From End of List.

"""

def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        fast = slow = dummy 
        
        # _ is not used in the loop can be any letter
        for _ in range(n): 
            # fast指向链表第n个元素
            fast = fast.next #
            
        # 直至fast=Null，此时slow指向倒数第n个元素。
        while fast.next is not None:
            fast = fast.next 
            slow = slow.next
        
        # skip the nth node
        slow.next = slow.next.next
        
        return dummy.next
