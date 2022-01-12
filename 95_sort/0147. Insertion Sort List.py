"""

Runtime: 204 ms, faster than 76.82% of Python3 online submissions for Insertion Sort List.
Memory Usage: 15.8 MB, less than 37.43% of Python3 online submissions for Insertion Sort List.

https://leetcode.com/problems/insertion-sort-list/discuss/190913/Java-Python-with-Explanations

"""

def insertionSortList(self, head):
    dummy = ListNode(0)
    dummy.next = head
    
    while head and head.next:
        if head.val > head.next.val:
            nodeToInsert = head.next
            nodeToInsertPre = dummy 
            # traverse from dummy
            while nodeToInsertPre.next.val < nodeToInsert.val:
                nodeToInsertPre = nodeToInsertPre.next
                
            head.next = nodeToInsert.next
            # insert nodeToInsert between nodeToInsertPre and nodeToInsertPre.next.
            nodeToInsert.next = nodeToInsertPre.next
            nodeToInsertPre.next = nodeToInsert
        else:
            head = head.next
        
    return dummy.next
    

