def preorderTraversal(self, root): 
    if not root: 
        return []

    stack = [root] 
    res = [] 

    while stack: 
        node = stack.pop() 
        res.append(node.val) 
        if node.right: 
            stack.append(node.right)
        if node.left: 
            stack.append(node.left) 

    return res

###

def preorderTraversal(self, root):
     res, stack = [], []
     node = root 
     while node or stack:
         while node:
             res.append(node.val)
             stack.append(node)
             node = node.left
         node = stack.pop()
         node = node.right
     
     return res
