def funWithAnagrams(arr):
    ans = []
    dic = {}
 
    for i in range(len(arr)):
        word = " ".join(sorted(arr[i]))
        if word not in dic:
            ans.append(arr[i])
            dic[word] = 1
    return sorted(ans)
