def findSubTree(self, root)：
    self.max_sum = -sys.maxint
    self.res = root
    self.get_sum(root)
    return self.res

def get_sum(self, root):
    if not root:
        return 0
    left = self.get_sum(root.left)
    right = self.get_sum(root.right)
    sum = root.val + left + right
    if sum > self.max_sum:
        self.max_sum = sum
        self.res = node
    return sum

//

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the maximum weight node
    import sys
    maximum_weight = 0
    result = None

    def findSubtree(self, root):
        # Write your code here
        self.helper(root)

        return self.result

    def helper(self, root):
        if root is None:
            return 0

        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)
        
        if left_weight + right_weight + root.val >= self.maximum_weight or self.result is None:
            self.maximum_weight = left_weight + right_weight + root.val
            self.result = root

        return left_weight + right_weight + root.val
