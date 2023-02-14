from collections import deque

def solve(eq):
    adj_list, indegree = {}, {}
    top = [None] * len(eq)
    
    # 初始化indegree
    for e in eq:
        e_arr = e.split() # ['A','=','B','+','C']
        indegree[e_arr[0]] = 0 # {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    
    # build dependency map
    for e in eq:
        e_arr = e.split()
        dest = e_arr[0] # 'A'
        for i in range(2, len(e_arr)): # A = B + C, 从 B 开始
            if 'A' <= e_arr[i][0] <= 'Z': # 是字母
                temp = adj_list.get(e_arr[i], [])
                temp.append(dest)
                adj_list[e_arr[i]] = temp # {B: A}, {C: A}
                indegree[dest] = indegree.get(dest, 0) + 1 # {A:1, B:0, C:0, D:0} # {A:2}
                # indegree: # {'A': 2, 'B': 2, 'C': 0, 'D': 0}
    
    # q stores indegree == 0 items to start with
    q = deque()
    for key, value in indegree.items():
        if value == 0:
            q.append(key) # ['C', 'D']
            
    # 顺序
    i = 0
    while q:
        top[i] = q.popleft()
        if top[i] in adj_list:
            for t in adj_list[top[i]]:
                indegree[t] -= 1
                if indegree[t] == 0:
                    q.append(t)
        i += 1
    # top = ['C', 'D', 'B', 'A']

    res = {}
    prev_eq = '+'
    for k in range(len(top)):
        total = 0
        for e in eq:
            e_arr = e.split()
            if e_arr[0] != top[k]: # 从C开始
                continue
            for j in range(2, len(e_arr)):
                if e_arr[j] == '+' or e_arr[j] == '-':
                    prev_eq = e_arr[j]
                elif 'A' <= e_arr[j][0] <= 'Z':
                    number = res[e_arr[j]]
                else:
                    number = int(e_arr[j])

                if prev_eq == '+':
                    total += number
                else:
                    total -= number

            res[top[k]] = total # {'C': 4, 'D': 6, 'B': 25, 'A': 54}
            break
    
    # 最终结果
    arr = []
    for key, value in res.items():
        arr.append(key + '=' + str(value))

    return arr
