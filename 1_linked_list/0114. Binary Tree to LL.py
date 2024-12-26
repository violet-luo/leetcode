def flatten(self, root: Optional[TreeNode]) -> None:
    if root is None:
        return None
    left_tail = self.flatten(root.left) # 2 -> 3 -> 4, left_tail = 4
    right_tail = self.flatten(root.right) # 5 -> 6, right_tail = 6
    if left_tail:
        left_tail.right = root.right  # 2 -> 3 -> 4 -> 5 -> 6
        root.right = root.left  # 1 -> 2 -> 3 -> 4 -> 5 -> 6
        root.left = None
    # fall for left tail: 1只有左子树2
    # fall for root: 只有1
    return right_tail or left_tail or root
        
###

def flatten(self, root):
    self.flatten_and_return_last_node(root)

def flatten_and_return_last_node(self, root):
    if not root:
        return

    left_last = self.flatten_and_return_last_node(root.left)
    right_last = self.flatten_and_return_last_node(root.right)

    #connect left_last to root.right
    if left_last:
        #以下顺序不能变，不然会被cover
        left_last.right = root.right # 4 -> 5
        root.right = root.left # 1 -> 2
        root.left = None 

    return right_last or left_last or root # 优先右子树再左子树再根
