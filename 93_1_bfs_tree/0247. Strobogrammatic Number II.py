def findStrobogrammatic(self, n): #2
    dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    queue, res = collections.deque(), []

    if n % 2 == 0:
        queue.append('') # 偶数长的数字
    else: # 奇数长的数字中间是0或1或8
        queue.append('0')
        queue.append('1')
        queue.append('8')

    res = []
    while queue:
        num = queue.popleft() # ''
        if len(num) == n: 
            if num[0] != '0' or n == 1: # 零开头的数
                res += [num]
        else:
            for key, val in dic.items():
                queue.append(key + num + val) # ['00','11','69','88','96']

    return res
