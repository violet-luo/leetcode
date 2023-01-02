def flatten(self, root):
    self.flatten_and_return_last_node(root)

def flatten_and_return_last_node(self, root):
    if root is None:
        return None

    left_last = self.flatten_and_return_last_node(root.left)
    right_last = self.flatten_and_return_last_node(root.right)

    #connect
    if left_last is not None:
        #以下顺序不能变，不然会被cover
        left_last.right = root.right
        root.right = root.left 
        root.left = None 

    return right_last or left_last or root
