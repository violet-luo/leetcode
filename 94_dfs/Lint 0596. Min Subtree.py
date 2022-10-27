def findSubTree(self, root)：
    self.min_sum = sys.maxint
    self.res = root
    self.get_sum(root)
    return self.res

def get_sum(self, root):
    if not root:
        return 0
    left = self.get_sum(root.left)
    right = self.get_sum(root.right)
    sum = root.val + left + right
    if sum < self.min_sum:
        self.min_sum = sum
        self.res = node
    return sum

//

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    import sys
    min_weight = 0
    result = None

    def findSubtree(self, root):
        self.helper(root)
        return self.result

    def helper(self, root):
        if root is None:
            return 0 
        
        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)
        
        if left_weight + right_weight + root.val <= self.min_weight or self.result is None:
            self.min_weight = left_weight + right_weight + root.val
            self.result = root

        return left_weight + right_weight + root.val
