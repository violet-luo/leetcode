class Solution:
    def sortedListToBST(self, head):
        return self.buildTree(head, None)

    def getMedian(self, left, right):
        fast = slow = left
        while fast != right and fast.next != right:
            slow = slow.next
            fast = fast.next.next
        return slow

    def buildTree(self, left, right):
        if left == right:
            return 
        mid = self.getMedian(left, right)
        root = TreeNode(mid.val)
        root.left = self.buildTree(left, mid)
        root.right = self.buildTree(mid.next, right)
        return root
