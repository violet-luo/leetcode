class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        # 1. find the first point, aka the left leaf
        while root != None:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        res = node
        node = node.right
        # 如果当前节点没有右子树，就返回当前节点
        # 如果当前节点有右子树，把当前右子树的所有左子树压入栈
        while node:
            self.stack.append(node)
            node = node.left
        return res

    def hasNext(self) -> bool:
        return len(self.stack) > 0
