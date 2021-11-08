"""

Runtime: 100 ms, faster than 64.78% of Python3 online submissions for Reorder List.
Memory Usage: 23.1 MB, less than 83.81% of Python3 online submissions for Reorder List.

"""

def reorderList(self, head: ListNode) -> None:
    if head is None:
        return None

    slow = fast = head

    # 1. 先找到中点
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. 把后半段倒过来
    prev, slow.next, slow = None, None, slow.next
    while slow:
        prev, prev.next, slow = slow, prev, slow.next
        
    # 3. 前后交替合并
    slow = head
    while prev:
        slow.next, slow = prev, slow.next
        prev.next, prev = slow, prev.next
