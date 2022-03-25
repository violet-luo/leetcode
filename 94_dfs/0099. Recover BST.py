class Solution:
    def recoverTree(self, root):
        if not root:
            return
        self.pre, self.first, self.second = None, None, None
        self.inOrder(root)
        if self.first:
            self.first.val, self.second.val = self.second.val, self.first.val
        return root

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        if self.pre:
            if not self.first and self.pre.val > root.val:
                self.first = self.pre
                self.second = root
            elif self.first and self.pre.val > root.val:
                self.second = root
        self.pre = root
        self.inOrder(root.right)
