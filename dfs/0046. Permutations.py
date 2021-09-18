def permute(self, nums):
    if not nums:
        return [[]]
        
    permutations = []
    self.dfs(nums, [], set(), permutations)
    return permutations

# 递归的定义：找到所有 permutation 开头的 permutations
def dfs(self, nums, permutation, visited, permutations):
    # 递归的出口，当n个数都记录到了，记录下来
    if len(nums) == len(permutation):
        permutations.append(list(permutation))
        return
    
    # 递归的拆解
    # [] => [1] [2] [3]
    # [1] => [1,2], [1,3], [1,4]
    for num in nums:
        if num in visited:
            continue
        permutation.append(num)
        visited.add(num)
        self.dfs(nums, permutation, visited, permutations)
        visited.remove(num)
        permutation.pop()
