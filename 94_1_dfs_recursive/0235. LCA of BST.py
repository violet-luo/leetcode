def lowestCommonAncestor(self, root, p, q):
    if root == p or root == q: # 这个别忘了
        return root
    if p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q
    if p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
    # p, q 分别在左右子树，那么root即为结果
    return root
