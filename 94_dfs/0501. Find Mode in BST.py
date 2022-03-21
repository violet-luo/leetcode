def findMode(self, root):
    if not root:
        return []
    dic = {}

    def dfs(root):
        if not root:
            return 
        if root.val not in dic:
            dic[root.val] = 1
        else:
            dic[root.val] += 1
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    mode = max(dic.values())
    return [key for key in dic.keys() if dic[key] == mode] 
