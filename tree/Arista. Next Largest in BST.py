def next_largest(node):
    # 1. 如果有右子树
    if node.right:
        node = node.right
        # 1.1 如果右子树有左子树
        while node.left:
            node = node.left
        # 1.2 如果右子树无左子树
        return node
        
    # 2. 如果无右子树
    while node.parent:
        # 2.1 如果是parent的左子树
        if node.parent.left == node:
            return node.parent
        # 2.2 如果是parent的右子树
        node = node.parent
    
    # 2.3 如果root没有右子树 或是一路都是右子树 即node是最大的数
    return None
