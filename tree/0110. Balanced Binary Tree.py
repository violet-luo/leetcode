"""

Runtime: 56 ms, faster than 68.45% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 17.2 MB, less than 97.11% of Python3 online submissions for Balanced Binary Tree.

"""

def isBalanced(self, root):
    if not root:
        return True
    
    if not self.isBalanced(root.left):
        return False
    if not self.isBalanced(root.right):
        return False
    
    return abs(self.get_height(root.left) - self.get_height(root.right)) <= 1
    

def get_height(self, root):
    if not root:
        return 0
    return max(self.get_height(root.left), self.get_height(root.right)) + 1
