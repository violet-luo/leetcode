def findSubtree(self, root):
    minimum, subtree, sum_of_root = self.helper(root)
    return subtree

def helper(self, root):
    if root is None:
        return sys.maxsize, None, 0

    left_minimum, left_subtree, left_sum = self.helper(root.left)
    right_minimum, right_subtree, right_sum = self.helper(root.right)

    sum_of_root = left_sum + right_sum + root.val 
    if left_minimum == min(left_minimum, right_minimum, sum_of_root):
        return left_minimum, left_subtree, sum_of_root
    if right_minimum == min(left_minimum, right_minimum, sum_of_root):
        return right_minimum, right_subtree, sum_of_root

    return sum_of_root, root, sum_of_root
