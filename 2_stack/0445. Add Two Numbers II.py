def addTwoNumbers(self, l1, l2):
    # 构建链表
    st1, st2 = [], []
    while l1:
        st1.append(l1.val)
        l1 = l1.next
    while l2:
        st2.append(l2.val)
        l2 = l2.next
    
    carry = 0
    dummy = ListNode(0)

    while st1 or st2 or carry != 0:
        digit1 = st1.pop() if st1 else 0
        digit2 = st2.pop() if st2 else 0
        sum = digit1 + digit2 + carry
        carry = 1 if sum >= 10 else 0
        sum = sum - 10 if sum >= 10 else sum
        # dummy -> cur
        cur = ListNode(sum)
        cur.next = dummy.next
        dummy.next = cur
          
    return dummy.next
