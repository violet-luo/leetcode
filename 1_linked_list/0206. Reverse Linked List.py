def reverse(self, head):
    #curt表示前继节点
    curt = None
    while head != None:
        #temp记录下一个节点，head是当前节点
        temp = head.next
        head.next = curt
        curt = head
        head = temp
    return curt
