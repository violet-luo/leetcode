def __init__(self, nestedList):
        self.next_elem = None
        # 对于nestedList中的内容，我们需要从左往右遍历，但堆栈pop是从右端开始，所以我们压栈的时候需要将nestedList反转再压栈
        self.stack = nestedList[::-1]
        
    # @return {int} the next element in the iteration
    def next(self):
        return self.next_elem
        
    # @return {boolean} true if the iteration has more element or false
    # 在while语句中查找拆解所有的list并按照顺序在next()中pop()
    def hasNext(self):
        while self.stack:
            cur = self.stack[-1] # [1,1]
            if cur.isInteger():
                self.next_elem = cur.getInteger()
                return True
            else: # cur is list
                cur_l = cur.getList()
                while cur_l:
                    self.stack.append(cur_l.pop())
        return False
