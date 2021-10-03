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
