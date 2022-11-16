def splitListToParts(self, head, k):
    length = 0
    cur = head

    #  1. 得到链表长度
    while cur:
        length += 1
        cur = cur.next

    # 2. 前 remainder 个部分的长度为 quotient+1，其余每个部分的长度各为 quotient
    quotient = length // k
    remainder = length % k

    parts = []
    prev = ListNode(0)
    cur = head

    for i in range(k):
        if cur:
            parts.append(cur)
            part_len = quotient+1 if remainder > 0 else quotient
            remainder -= 1
            for j in range(part_len):
                prev, cur = cur, cur.next
            prev.next = None  # cut here
        else: # [1,2,3], 5 -> [[1],[2],[3],[],[]]
            parts.append(None)
    return parts
