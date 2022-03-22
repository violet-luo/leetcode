class Solution(object):
    pre, res = -float('inf'), float('inf')
    
    # [1,3,4,5,6,7,8]
    def minDiffInBST(self, root): #minDiff(3) #minDiff(4)
        # 前序遍历
        if root.left:
            self.minDiffInBST(root.left)
        # 中序遍历
        self.res = min(self.res, root.val - self.pre) # 3-1=2 #4-3=1
        self.pre = root.val #之前minDiff走过的结点
        # 后序遍历
        if root.right:
            self.minDiffInBST(root.right)
        return self.res
