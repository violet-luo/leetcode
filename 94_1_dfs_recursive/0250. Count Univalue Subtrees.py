def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
    cnt = 0

    def is_unival(node):
        if node is None:
            return True
        nonlocal cnt

        left_unival = is_unival(node.left)
        right_unival = is_unival(node.right)

        if left_unival and right_unival:
            if node.left and node.right:
                if node.left.val == node.right.val == node.val:
                    cnt += 1
                    return True
            elif node.left:
                if node.left.val == node.val:
                    cnt += 1
                    return True
            elif node.right:
                if node.right.val == node.val:
                    cnt += 1
                    return True
            else:
                cnt += 1 
                return True
            return False

    is_unival(root)
    return cnt

###

def countUnivalSubtrees(self, root):
    res = 0
    def dfs(node) -> int:
        if not node:
            return None
        if not node.left and not node.right:
            nonlocal res
            res += 1
            return node.val
        left = dfs(node.left)
        right = dfs(node.right)
        if left == right == node.val or (not left and right == node.val) or (not right and left == node.val):
            res += 1
            return node.val
        return float('inf')
    
    dfs(root)
    return res

###

def countUnivalSubtrees(self, root):
    count = 0

    def dfs(root):
        if not root:
            return True
        l = dfs(root.left)
        r = dfs(root.right)
        # if both children are "True" and root.val is equal to both children's values if exist
        if l and r and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
            nonlocal count
            count += 1
            return True
        return False

    dfs(root)
    return count

###

def countUnivalSubtrees(self, root):
    self.count = 0
    self.dfs(root)
    return self.count

def dfs(self, root):
    if not root:
        return True
    l = self.dfs(root.left)
    r = self.dfs(root.right)
    # if both children are "True" and root.val is equal to both children's values if exist
    if l and r and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
        self.count += 1
        return True
    return False
