def lowestCommonAncestor(self, root, A, B):
    if root is None:
        return None

    if root == A or root == B:
        return root 

    # 找 A 和 B
    left_result = self.lowestCommonAncestor(root.left, A, B)
    right_result = self.lowestCommonAncestor(root.right, A, B)

    # A 和 B 一边一个
    if left_result and right_result: 
        return root

    # 左子树有一个点或者左子树有LCA
    if left_result:
        return left_result

    # 右子树有一个点或者右子树有LCA
    if right_result:
        return right_result

    # 左右子树啥都没有
    return None
