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
