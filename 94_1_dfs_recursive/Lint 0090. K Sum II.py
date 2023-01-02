class Solution:
    def kSumII(self, A, k, target):
        A = sorted(A) #按照字母序得到结果，相同的字母在一起，方便去重
        subsets = []
        self.dfs(A, 0, k, target, [], subsets)
        return subsets
    
    # 从A的index位置开始，选k个数字放入subset, 满足k个数字和为target
    def dfs(self, A, index, k, target, subset, subsets):
        if k == 0 and target == 0:
            subsets.append(list(subset))
            return
        
        # 同样是递归出口
        # 1. 0个数字之和为非0target,即已经用完了数字，没得到目标和
        # 2. 剩下数字之和为负数，即规定的k个数字还没用完，但是和已经大于等于目标和
        if k == 0 or target <= 0:
            return
        
        for i in range(index, len(A)):
            subset.append(A[i])
            self.dfs(A, i + 1, k - 1, target - A[i], subset, subsets)
            subset.pop()
