"""

Runtime: 36 ms, faster than 78.77% of Python3 online submissions for Rotate List.
Memory Usage: 13.7 MB, less than 83.19% of Python3 online submissions for Rotate List.

"""

def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if head is None:
        return None

    slow = fast = head
    length = 1

    while fast and fast.next:
        fast = fast.next
        length += 1

    # LL Cycle
    fast.next = head

    # k might be longer than the length
    k %= length

    for _ in range(length-k-1):
        slow = slow.next 
    ans = slow.next
    slow.next = None
    return ans
