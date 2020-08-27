"""

Runtime: 72 ms, faster than 81.98% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 24.1 MB, less than 49.02% of Python3 online submissions for Palindrome Linked List.

https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).

"""

def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
        
        # reverse the second half
        bottom = None
        while slow:
            nxt = slow.next 
            slow.next = bottom
            bottom = slow 
            slow = nxt 
        # compare the first and second half
        while bottom:
            if bottom.val != head.val:
                return False
            head, bottom = head.next, bottom.next
        return True
